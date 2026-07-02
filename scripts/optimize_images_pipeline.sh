#!/bin/bash
# Image Optimization Pipeline — runs before Hugo build
# Converts any remaining PNGs to WebP, generates 600px thumbnails,
# and ensures all images are optimized.
#
# Usage: ./scripts/optimize_images_pipeline.sh
# Called by: GitHub Actions deploy workflow (pre-build step)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
IMAGES_DIR="${REPO_ROOT}/static/images"

if ! command -v cwebp &>/dev/null; then
    echo "Installing webp tools..."
    if command -v apt-get &>/dev/null; then
        sudo apt-get install -y webp
    elif command -v brew &>/dev/null; then
        brew install webp
    else
        echo "ERROR: Cannot install cwebp. Please install manually."
        exit 1
    fi
fi

echo "=== Image Optimization Pipeline ==="

# Step 1: Convert any remaining PNGs to WebP
PNG_COUNT=0
while IFS= read -r -d '' png_file; do
    webp_file="${png_file%.png}.webp"
    if [[ ! -f "$webp_file" ]]; then
        cwebp -q 82 -resize 1200 0 "$png_file" -o "$webp_file" -quiet 2>/dev/null && rm "$png_file"
        PNG_COUNT=$((PNG_COUNT + 1))
    fi
done < <(find "$IMAGES_DIR" -name "*.png" -type f -print0 2>/dev/null)
echo "Converted ${PNG_COUNT} new PNGs to WebP"

# Step 1b: Fix any .png references in content frontmatter to .webp
CONTENT_DIR="${REPO_ROOT}/content"
FIX_COUNT=0
while IFS= read -r -d '' md_file; do
    if grep -q '\.png"' "$md_file"; then
        sed -i 's|\.png"|\.webp"|g' "$md_file"
        FIX_COUNT=$((FIX_COUNT + 1))
    fi
done < <(find "$CONTENT_DIR" -name "*.md" -type f -print0 2>/dev/null)
if [[ $FIX_COUNT -gt 0 ]]; then
    echo "Fixed ${FIX_COUNT} markdown files with .png → .webp refs"
fi

# Step 2: Generate thumbnails (600px) for all WebP images
THUMB_COUNT=0
while IFS= read -r -d '' webp_file; do
    dir=$(dirname "$webp_file")
    base=$(basename "$webp_file" .webp)
    thumb_file="${dir}/${base}-thumb.webp"

    # Skip if already a thumbnail
    [[ "$base" == *-thumb ]] && continue

    # Skip if thumbnail exists and is newer
    [[ -f "$thumb_file" && "$thumb_file" -nt "$webp_file" ]] && continue

    # Generate 600px wide thumbnail
    cwebp -q 75 -resize 600 0 "$webp_file" -o "$thumb_file" -quiet 2>/dev/null
    THUMB_COUNT=$((THUMB_COUNT + 1))
done < <(find "$IMAGES_DIR" -name "*.webp" -type f -print0 2>/dev/null)
echo "Generated ${THUMB_COUNT} thumbnails"

# Step 3: Report final size
TOTAL_SIZE=$(du -sh "$IMAGES_DIR" 2>/dev/null | awk '{print $1}')
echo "Total images directory: ${TOTAL_SIZE}"
echo "=== Pipeline Complete ==="
