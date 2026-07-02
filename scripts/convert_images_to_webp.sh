#!/bin/bash
# Convert all PNG images to WebP at 1200px max width
# Expected savings: 80-90% (~400+ MB)
# Requires: cwebp (brew install webp) and sips

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
IMAGES_DIR="${REPO_ROOT}/static/images"
CONTENT_DIR="${REPO_ROOT}/content"

if ! command -v cwebp &>/dev/null; then
    echo "ERROR: cwebp not found. Install with: brew install webp"
    exit 1
fi

echo "=== PNG to WebP Conversion Pipeline ==="
echo "Images dir: ${IMAGES_DIR}"
echo ""

TOTAL=0
CONVERTED=0
SKIPPED=0
SAVED_BYTES=0

# Find all PNG files
while IFS= read -r -d '' png_file; do
    TOTAL=$((TOTAL + 1))
    webp_file="${png_file%.png}.webp"

    # Skip if WebP already exists and is newer
    if [[ -f "$webp_file" && "$webp_file" -nt "$png_file" ]]; then
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    # Get original dimensions
    orig_width=$(sips -g pixelWidth "$png_file" 2>/dev/null | awk '/pixelWidth/{print $2}')
    orig_size=$(stat -f%z "$png_file" 2>/dev/null || stat -c%s "$png_file" 2>/dev/null)

    # Determine resize flag (max 1200px width)
    resize_flag=""
    if [[ -n "$orig_width" && "$orig_width" -gt 1200 ]]; then
        resize_flag="-resize 1200 0"
    fi

    # Convert to WebP (quality 82 is a good balance for generated art)
    if cwebp -q 82 $resize_flag "$png_file" -o "$webp_file" -quiet 2>/dev/null; then
        new_size=$(stat -f%z "$webp_file" 2>/dev/null || stat -c%s "$webp_file" 2>/dev/null)
        saved=$((orig_size - new_size))
        SAVED_BYTES=$((SAVED_BYTES + saved))
        CONVERTED=$((CONVERTED + 1))

        # Remove original PNG after successful conversion
        rm "$png_file"
    else
        echo "  WARN: Failed to convert: $png_file"
    fi
done < <(find "$IMAGES_DIR" -name "*.png" -type f -print0)

echo ""
echo "=== Conversion Complete ==="
echo "Total PNGs found: ${TOTAL}"
echo "Converted: ${CONVERTED}"
echo "Skipped (already done): ${SKIPPED}"
echo "Space saved: $((SAVED_BYTES / 1024 / 1024)) MB"
echo ""

# Now update all content files to reference .webp instead of .png
echo "=== Updating content references ==="
REF_COUNT=0

while IFS= read -r -d '' md_file; do
    if grep -q '\.png' "$md_file"; then
        # Replace .png references in image paths (cover images, inline images)
        sed -i '' 's|\.png"|\.webp"|g' "$md_file"
        sed -i '' 's|\.png)|\.webp)|g' "$md_file"
        # Handle cases without trailing quote/paren (end of line)
        sed -i '' 's|\.png$|\.webp|g' "$md_file"
        REF_COUNT=$((REF_COUNT + 1))
    fi
done < <(find "$CONTENT_DIR" -name "*.md" -type f -print0)

# Also update hugo.yaml if it references any images
if grep -q '\.png' "${REPO_ROOT}/hugo.yaml"; then
    sed -i '' 's|\.png|\.webp|g' "${REPO_ROOT}/hugo.yaml"
fi

echo "Updated ${REF_COUNT} content files"
echo ""
echo "Done. Run 'hugo --gc --minify' to verify build."
