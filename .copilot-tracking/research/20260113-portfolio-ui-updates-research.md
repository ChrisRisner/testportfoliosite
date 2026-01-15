<!-- markdownlint-disable-file -->
# Task Research Documents: Portfolio UI Updates (V2)

Researching and planning UI updates for the portfolio site, specifically focusing on the navigation menu alignment, image hover effects, and image linking behavior.

## Task Implementation Requests
<!-- <per_tasks_for_implementation> -->
* Update left menu alignment: sticky/fixed behavior vs scrolling, and horizontal text alignment.
* Update hover overlay size to cover 80% of the underlying image.
* Change album image click behavior to navigate to standalone album pages instead of using data injection.
<!-- <per_tasks_for_implementation> -->

## Scope and Success Criteria
* Scope: `src/static/style.css`, `src/templates/index.html`, `src/static/app.js`.
* Assumptions: The site uses a build script (`src/build.py`) to generate static pages.
* Success Criteria:
  * Left menu scrolls with the page and text is horizontally centered in the column.
  * Hover overlay covers 80% of the image.
  * Clicking an album image navigates to the specific album's page without JS interception.

## Outline
* Research Current Implementation
    * Menu CSS/HTML
    * Hover CSS
    * Image Click Logic
* Develop Solution
    * CSS Logic for Menu
    * CSS Logic for Hover
    * HTML/JS Change for Links

## Research Executed

### File Analysis
* `src/templates/index.html`
  * Correctly renders static HTML for both Home (list of albums) and Album (gallery) views using Jinja2 logic (`{% if current_album %}`).
  * Uses standard URL links (`href="/{{ album.slug }}/"`).
* `src/static/style.css`
  * `.sidebar` uses `position: sticky`, `height: 100vh`, and `justify-content: center`. This keeps it pinned and vertically centered.
  * `.album-card h3` uses `min-width: 60%` for the hover overlay.
* `src/static/app.js`
  * Contains logic that overrides the server-rendered HTML.
  * `document.addEventListener('DOMContentLoaded', ...)` calls `handleNavigation`, which wipes `content.innerHTML` and re-renders the page using client-side data (`window.portfolioData`).
  * The client-side `renderHome` function creates links with hash fragments (`#slug`), causing the "app-like" behavior the user wants to remove.
* `src/build.py`
  * Confirmed: Generates individual HTML files for each album in subdirectories (e.g., `output/drink/index.html`). This validates that we can safely remove the client-side router.

### Code Search Results
* Confirmed `window.portfolioData` injection in `index.html`.

## Key Discoveries

### Project Structure
* **Hybrid Approach:** The project currently mixes server-side generation (Python/Jinja) with client-side SPA routing (JS). This causes the conflict where correct static links are replaced by JS hash links.
* **Build Capability:** `build.py` already supports full static site generation with sub-pages, so the SPA logic is entirely redundant.

### Implementation Patterns
* **Sidebar:** Flexbox column with sticky positioning.
* **Hover Overlay:** Absolute positioning on an `h3` element inside the card.
* **Navigation:** Currently hijacked by `app.js` to act as a Single Page App.
* **Lightbox:** `app.js` manually constructs PhotoSwipe instances from data. The standard approach is to initialize it on existing DOM elements (anchors).

### Complete Examples
```css
/* Sidebar Fix */
.sidebar {
    background-color: var(--sidebar-bg);
    padding: 2rem;
    /* Removed height: 100vh, sticky, top: 0, overflow-y */
    /* width: var(--sidebar-width); - Keep this */
    flex-shrink: 0;
    display: flex;
    flex-direction: column;
    /* Removed justify-content: center */
    text-align: center; /* Center text horizontally */
    align-items: center; /* Center flex items horizontally */
    min-height: 100vh; /* Keep min-height to ensure column look if needed */
    height: auto;
    position: static; /* Not sticky */
}

/* Hover Box Fix */
.album-card h3 {
    /* ... positioning ... */
    width: 80%; /* Was min-width: 60% */
    /* ... styles ... */
}
```

## Technical Scenarios

### 1. UI Updates
* **Sidebar:** Switch to standard document flow (non-sticky) and center content horizontally.
* **Hover:** Increase overlay width to 80%.
* **Navigation:** Disable JS routing. Rely on `index.html` server-rendered links. `app.js` should only handle the Lightbox for the album view on an as-needed basis.

**Preferred Approach:**
1.  **CSS:** Update `.sidebar` and `.album-card h3`.
2.  **JS:** Massive simplification of `app.js`. Remove `handleNavigation`, `renderHome`, `renderAlbum`, `updateActiveLink`.
3.  **HTML:** Remove the data injection script and update the gallery markup to be PhotoSwipe-friendly (using `<a>` tags).

**Implementation Details:**

*   **`src/static/app.js`**:
    *   Remove all routing and rendering logic.
    *   Retain `PhotoSwipeLightbox` imports.
    *   On `DOMContentLoaded`, check for `.album-grid` (or a specific gallery ID/class).
    *   Initialize `PhotoSwipeLightbox` targeting the child `a` tags.
*   **`src/templates/index.html`**:
    *   Remove `<script>window.portfolioData = ...</script>`.
    *   Update the `{% for photo in current_album.photos %}` loop:
        *   Change outer wrapper from `<div class="photo-link">` to `<a href="{{ photo.src }}" class="photo-link" data-pswp-width="..." data-pswp-height="..." target="_blank">`.
        *   Keep inner `<img>`.
*   **`src/static/style.css`**:
    *   `.sidebar`: Remove `position: sticky`, `height: 100vh`. Add `min-height: 100vh`, `text-align: center`, `align-items: center`.
    *   `.album-card h3`: Change `min-width: 60%` to `width: 80%`.

#### Considered Alternatives (Removed After Selection)
*   **Keep SPA logic but just fix links:** Too complex and error-prone. The user specifically asked to remove "data injection", implying they want standard static pages.
