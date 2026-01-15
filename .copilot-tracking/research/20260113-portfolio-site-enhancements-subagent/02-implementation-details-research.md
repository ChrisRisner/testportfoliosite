# Implementation Details Research
*Date: 2026-01-13*

## 1. Project Architecture Analysis
*   **Type:** Hybrid Static Site.
*   **Build System:** `src/build.py` generates a single static `index.html` containing the database JSON.
*   **Routing:** `src/static/app.js` handles client-side routing using `window.location.hash`.
*   **Conclusion:** The requested "Home Page" functionality must be implemented in `app.js` (client-side) rather than generating a separate physical page, to maintain the SPA transitions.

## 2. File-Specific Modifications

### A. Home Page Logic (`src/static/app.js`)
**Goal:** Prevent auto-redirect to first album when URL is empty. Render a grid of albums instead.

**Current Logic:**
```javascript
// Default to first album if no hash or invalid hash
if (!activeAlbum && db.albums.length > 0) {
    activeAlbum = db.albums[0];
}
```

**Target Logic:**
```javascript
// If no hash, render the Home Grid
if (!hash) {
    renderHome(db);
    return;
}
```

**New Function Needed:** `renderHome(db)`
*   Clears content.
*   Loops through `db.albums`.
*   Renders clickable "Card" using `album.cover` image.
*   Links to `#{album.slug}`.

### B. HTML Structure (`src/templates/index.html`)

**Goal 1: Sidebar Title**
*   **Current:** Sidebar only contains `<nav>`.
*   **Target:** Add `<h1>` before `<nav>`.

**Goal 2: Mobile Header (Title Center, Hamburger Right)**
*   **Current:** Button first, H1 second. Flex `space-between`.
*   **Target:** Swap order or use Flexbox tricks. Swapping order puts Button on right naturally if we use `justify-content: space-between`.
    *   *Correction:* To strictly center the Title, we need to be careful. If we want Button on Right and Title Center, we can put Title first (centered) and absolute position the button, or use a 3-column flex grid (invisible left element).
    *   *Chosen Approach:* Swap HTML order to `H1`, `Button`. Use Flexbox to align.

**Current HTML:**
```html
<header class="mobile-header">
    <button id="menu-toggle" aria-label="Toggle Menu">☰</button>
    <h1>Portfolio</h1>
</header>
```

**Target HTML:**
```html
<header class="mobile-header">
    <h1 class="header-title">Portfolio</h1> <!-- Link to home # -->
    <button id="menu-toggle" aria-label="Toggle Menu">☰</button>
</header>
```

### C. Styling (`src/static/style.css`)

**Goal 1: CSS Grid (2 per row)**
*   **Current:** `.album-grid` uses `repeat(auto-fill, minmax(250px, 1fr))`.
*   **Target:** Create specific class `.home-albums-grid` or modify existing rules.
    *   Mobile: 1 column?
    *   Desktop: 2 columns fixed?
    *   *Snippet:*
    ```css
    .home-grid {
        display: grid;
        grid-template-columns: 1fr 1fr; /* 2 per row */
        gap: 20px;
    }
    @media (max-width: 768px) {
        .home-grid { grid-template-columns: 1fr; }
    }
    ```

**Goal 2: Sidebar Styling**
*   **Current:** `background-color: var(--sidebar-bg);` (where `--sidebar-bg: #f5f5f5`).
*   **Target:** Update CSS variable or rule to White (`#ffffff`).
    *   *Snippet:* `:root { --sidebar-bg: #ffffff; }`

**Goal 3: Page Padding**
*   **Current:** `.content { padding: 2rem; }`
*   **Target:** Increase padding if "more whitespace" is requested, or ensure consistency. If specifically asked to "Add padding", simple adjustment here.

**Goal 4: Mobile Header Flex**
*   **Current:** `.mobile-header { justify-content: space-between; ... }`
*   **Target:**
    ```css
    .mobile-header {
        /* ... */
        justify-content: center; /* Center title */
        position: relative;
    }
    #menu-toggle {
        position: absolute;
        right: 1rem; /* Fix to right */
    }
    ```

## 3. Data Verification (`src/build.py`)
*   `db.json` structure: `albums` list contains objects with `cover` (path to thumbnail).
*   **Verdict:** No changes needed in Python. The data is already available for the JS renderer.

## 4. Execution Order
1.  **CSS:** Update variables and add `.home-grid` classes.
2.  **HTML:** Update Sidebar and Mobile Header structure.
3.  **JS:** Implement `renderHome` and update routing logic.
4.  **Test:** Verify Home view, Album view, and Mobile transitions.
