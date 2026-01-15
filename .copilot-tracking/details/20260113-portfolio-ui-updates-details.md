<!-- markdownlint-disable-file -->
# Task Details: Portfolio UI Updates

## Research Reference

**Source Research**: .copilot-tracking/research/20260113-portfolio-ui-updates-research.md

## Phase 1: CSS Styling Updates

### Task 1.1: Update Sidebar Styles

Remove sticky positioning and vertical centering from the sidebar. Instead, allow it to scroll naturally and center the text horizontally.

* **Files**:
  * `src/static/style.css` - Update `.sidebar` class.
* **Success**:
  * Sidebar is no longer `position: sticky`.
  * Text content is horizontally centered (`text-align: center`, `align-items: center`).
  * `height: 100vh` constraint is removed/relaxed to `min-height`.
* **Research References**:
  * .copilot-tracking/research/20260113-portfolio-ui-updates-research.md (Lines 80-92) - CSS Solution.

### Task 1.2: Update Album Card Hover Overlay

Increase the width of the hover text overlay on album cards to cover more of the image.

* **Files**:
  * `src/static/style.css` - Update `.album-card h3`.
* **Success**:
  * Overlay width is `80%`.
* **Research References**:
  * .copilot-tracking/research/20260113-portfolio-ui-updates-research.md (Lines 94-98) - CSS Solution.
* **Dependencies**:
  * Task 1.1 completion (CSS structural changes first).

## Phase 2: Core Logic Refactoring (HTML & JS)

### Task 2.1: Update HTML Template Structure

Remove data injection script and restructure the gallery loop to use standard `<a>` tags for PhotoSwipe, rather than a `div` that requires JS instantiation.

* **Files**:
  * `src/templates/index.html` - Remove `window.portfolioData`, update photo loop.
* **Success**:
  * No `<script>window.portfolioData = ...` in the output HTML.
  * Gallery items are wrapped in `<a href="..." target="_blank">` with PhotoSwipe data attributes (`data-pswp-width`, `data-pswp-height`).
* **Research References**:
  * .copilot-tracking/research/20260113-portfolio-ui-updates-research.md (Lines 113-118) - HTML Implementation Details.
* **Dependencies**:
  * Phase 1 completion.

### Task 2.2: Simplify JavaScript Logic

Remove all SPA routing logic (handleNavigation, renderHome, etc.) from `app.js`. Isolate PhotoSwipe initialization to run on the pre-rendered DOM elements.

* **Files**:
  * `src/static/app.js` - Remove routing, keep Lightbox init.
* **Success**:
  * Client-side routing is removed.
  * Clicking an album link performs a standard browser navigation.
  * PhotoSwipe initializes correctly on the gallery page.
* **Research References**:
  * .copilot-tracking/research/20260113-portfolio-ui-updates-research.md (Lines 105-111) - JS Implementation Details.
* **Dependencies**:
  * Task 2.1 completion (HTML structure must be ready for the simplified JS).

## Dependencies

* `build.py` execution to regenerate HTML files after template changes.

## Success Criteria

* Navigation works without hash fragments.
* UI matches the requested visual changes (Sidebar center, Hover 80%).
