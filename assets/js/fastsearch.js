// Project override of PaperMod's fastsearch.js (2026-10-19).
// - Index is the slim /index.json: {title, url, section, date (YYYY-MM-DD), summary (~300 chars)}.
// - Section + date filters (layouts/search.html); the filters narrow the result set, the query ranks it.
// - Reads ?q= / ?section= / ?days= / ?from= / ?to= on load and keeps the URL in sync (replaceState),
//   so the homepage search box (GET /search/?q=…) and shared links work. The extend_head handoff
//   script may also fill ?q= — both paths set the same value, so a double fill is harmless.
import * as params from '@params';

const resList = document.getElementById('searchResults');
const sInput = document.getElementById('searchInput');
const searchBox = document.getElementById('searchbox');
const fSection = document.getElementById('searchSection');
const fDays = document.getElementById('searchDays');
const fFrom = document.getElementById('searchFrom');
const fTo = document.getElementById('searchTo');
const status = document.getElementById('searchStatus');

let fuse;
let data = [];
let firstResult = null;
let lastResult = null;

const LIMIT = (params.fuseOpts && params.fuseOpts.limit) || 20;

const buildFuseOptions = () => {
    const o = params.fuseOpts || {};
    return {
        isCaseSensitive: o.iscasesensitive ?? false,
        minMatchCharLength: o.minmatchcharlength ?? 1,
        shouldSort: o.shouldsort ?? true,
        keys: o.keys ?? ['title', 'summary'],
        location: o.location ?? 0,
        threshold: o.threshold ?? 0.4,
        distance: o.distance ?? 100,
        ignoreLocation: o.ignorelocation ?? true
    };
};

const debounce = (fn, delay) => {
    let timeout;
    return (...args) => {
        clearTimeout(timeout);
        timeout = window.setTimeout(() => fn(...args), delay);
    };
};

const isoDaysAgo = (n) => {
    const d = new Date();
    d.setDate(d.getDate() - (n - 1));
    const pad = (x) => String(x).padStart(2, '0');   // local date, not UTC (evenings in PT)
    return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
};

// The active filters as {section, from, to} — empty strings mean "no limit".
const currentFilters = () => {
    let from = fFrom?.value || '';
    const days = parseInt(fDays?.value || '', 10);
    if (days > 0) {
        const d = isoDaysAgo(days);
        if (!from || d > from) from = d;
    }
    return { section: fSection?.value || '', from, to: fTo?.value || '' };
};

const passes = (item, f) =>
    (!f.section || item.section === f.section) &&
    (!f.from || item.date >= f.from) &&
    (!f.to || item.date <= f.to);

const syncUrl = () => {
    const u = new URL(location.href);
    const set = (k, v) => (v ? u.searchParams.set(k, v) : u.searchParams.delete(k));
    set('q', sInput.value.trim());
    set('section', fSection?.value);
    set('days', fDays?.value);
    set('from', fFrom?.value);
    set('to', fTo?.value);
    history.replaceState(null, '', u);
};

const el = (tag, cls, text) => {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text) e.textContent = text;
    return e;
};

const renderResults = (items, total) => {
    resList.innerHTML = '';
    firstResult = lastResult = null;
    if (status) status.textContent = total === null ? '' : `${total} match${total === 1 ? '' : 'es'}` +
        (total > items.length ? ` — showing ${items.length}` : '');
    if (!items.length) return;
    const fragment = document.createDocumentFragment();
    for (const item of items) {
        const li = document.createElement('li');
        li.appendChild(document.createTextNode(item.title));
        li.appendChild(el('span', 'nova-sr-meta', `${item.section} · ${item.date}`));
        if (item.summary) li.appendChild(el('span', 'nova-sr-sum', item.summary));
        const link = el('a', 'entry-link');
        link.href = item.url;
        link.setAttribute('aria-label', item.title);
        li.appendChild(link);
        fragment.appendChild(li);
    }
    resList.appendChild(fragment);
    firstResult = resList.firstElementChild;
    lastResult = resList.lastElementChild;
};

const performSearch = () => {
    if (!fuse) return;
    syncUrl();
    const query = sInput.value.trim();
    const f = currentFilters();
    const filtered = f.section || f.from || f.to;
    let items;
    if (query) {
        // Unfiltered: Fuse's own limit. Filtered: rank everything, then filter, then cut.
        const hits = filtered ? fuse.search(query) : fuse.search(query, { limit: LIMIT });
        items = hits.map((r) => r.item).filter((it) => passes(it, f));
    } else if (filtered) {
        // No query, filters only: newest first — "browse this section / this week".
        items = data.filter((it) => passes(it, f)).sort((a, b) => (a.date < b.date ? 1 : -1));
    } else {
        renderResults([], null);
        return;
    }
    renderResults(items.slice(0, LIMIT), filtered || !query ? items.length : null);
};

const initSearch = async () => {
    if (!sInput || !resList) return;
    const qs = new URLSearchParams(location.search);
    if (fSection && qs.get('section')) fSection.value = qs.get('section');
    if (fDays && qs.get('days')) fDays.value = qs.get('days');
    if (fFrom && qs.get('from')) fFrom.value = qs.get('from');
    if (fTo && qs.get('to')) fTo.value = qs.get('to');
    if (status) status.textContent = 'Loading index…';
    try {
        const response = await fetch('../index.json');
        if (!response.ok) throw new Error(`Search index load failed: ${response.status}`);
        data = (await response.json()) || [];
        fuse = new Fuse(data, buildFuseOptions());
        if (status) status.textContent = '';
    } catch (error) {
        console.error(error);
        if (status) status.textContent = 'Search index failed to load.';
    }
    sInput.disabled = false;
    if (qs.get('q')) sInput.value = qs.get('q');
    sInput.focus();
    performSearch();
};

window.addEventListener('load', initSearch);

sInput?.addEventListener('input', debounce(performSearch, 150));
for (const f of [fSection, fDays, fFrom, fTo]) f?.addEventListener('change', performSearch);

sInput?.addEventListener('search', () => {
    if (!sInput.value) performSearch();
});

document.addEventListener('keydown', (event) => {
    const { key } = event;
    const active = document.activeElement;
    const isInSearchBox = searchBox?.contains(active);

    if (key === 'Escape') {
        sInput.value = '';
        performSearch();
        sInput.focus();
        return;
    }
    if (!firstResult || !isInSearchBox) return;
    if (active !== sInput && !active?.matches?.('.entry-link')) return;   // leave selects/date inputs alone
    const focusLink = (li) => {
        document.querySelectorAll('.focus').forEach((i) => i.classList.remove('focus'));
        const a = li?.querySelector('.entry-link');
        if (a) { a.focus(); li.classList.add('focus'); }
    };
    if (key === 'ArrowDown') {
        event.preventDefault();
        if (active === sInput) focusLink(firstResult);
        else if (active?.parentElement !== lastResult) focusLink(active?.parentElement?.nextElementSibling);
    } else if (key === 'ArrowUp') {
        event.preventDefault();
        if (active?.parentElement === firstResult) sInput.focus();
        else if (active !== sInput) focusLink(active?.parentElement?.previousElementSibling);
    } else if (key === 'ArrowRight') {
        if (active?.matches?.('.entry-link')) active.click();
    }
});
