<!-- markdownlint-disable-file -->
# Task Details: Portfolio Site Enhancements

## Research Reference

**Source Research**: .copilot-tracking/research/20260113-portfolio-site-enhancements-research.md

## Phase 1: Static Site Generation

### Task 1.1: Update Template for Conditional Rendering

Modify `src/templates/index.html` to support server-side rendering of different views based on the presence of a `current_album` variable.

*   **Files**:
    *   [src/templates/index.html](src/templates/index.html) - The Jinja2 template.
*   **Success**:
    *   Template correctly renders the album grid when `current_album` is None.
    *   Template correctly renders photos of the `current_album` when it is provided.
*   **Research References**:
    *   .copilot-tracking/research/20260113-portfolio-site-enhancements-research.md (Lines 100-111) - Template logic snippet.
*   **Dependencies**:
    *   None

### Task 1.2: Update Build Script for Multi-page Generation

Refactor the manual page generation in `src/build.py` to loop through the constructed database and generate pages for the home view and each album folder.

*   **Files**:
    *   [src/build.py](src/build.py) - The static site generator script.
*   **Success**:
    *   Running `python src/build.py` creates `dist/index.html`.
    *   Running the script also creates directories in `dist/` matching album slugs, each containing an `index.html`.
*   **Research References**:
    *   .copilot-tracking/research/20260113-portfolio-site-enhancements-research.md (Lines 70-98) - Proposed python loop.
*   **Dependencies**:
    *   Task 1.1 (Template must accommodate the new variables).

## Phase 2: UI Enhancements

### Task 2.1: Center Sidebar Navigation

Update CSS to center the navigation links vertically within the sidebar.

*   **Files**:
    *   [src/static/style.css](src/static/style.css) - Stylesheet.
*   **Success**:
    *   `.nav-list` or its container uses Flexbox to center content vertically.
*   **Research References**:
    *   .copilot-tracking/research/20260113-portfolio-site-enhancements-research.md (Lines 20-25) - CSS findings for alignment.
*   **Dependencies**:
    *   None

### Task 2.2: Refine Album Card Hover Style

Adjust the hover effect on album cards to be less intrusive or better formatted.

*   **Files**:
    *   [src/static/style.css](src/static/style.css) - Stylesheet.
*   **Success**:
    *   The white overlay on `.album-card` hover is adjusted (padding/position) so it looks intentional and doesn't just block the whole image white.
*   **Research References**:
    *   .copilot-tracking/research/20260113-portfolio-site-enhancements-research.md (Lines 26-30) - CSS findings for hover effect.
*   **Dependencies**:
    *   None

## Dependencies

*   Python environment with `jinja2`, `Pillow` (as per requirements).

## Success Criteria

*   User can navigate from Home -> Album Page -> Back to Home using standard links (no JS routing required).
*   Visual layout matches user request ("Center nav", "Fix hover padding").
