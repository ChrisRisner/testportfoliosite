---
applyTo: '.copilot-tracking/changes/20260113-portfolio-ui-updates-changes.md'
---
<!-- markdownlint-disable-file -->
# Task Checklist: Portfolio UI Updates

## Overview

Update navigation menu alignment, adjust image hover overlay size, and refactor the site to use standard static navigation instead of client-side routing.

Follow all instructions from #file:../../.github/instructions/task-implementation.instructions.md

## Objectives

* Center sidebar text horizontally and remove sticky behavior.
* Increase album card hover overlay to cover 80% of the image.
* Remove client-side router (`app.js`) and rely on server-generated static files.
* Update Lightbox implementation to work with standard `<a>` tags.

## Research Summary

### Project Files
* `src/static/style.css` - Contains sidebar and card styles.
* `src/templates/index.html` - Jinja2 template rendering the HTML structure.
* `src/static/app.js` - Currently handles SPA routing and data injection.

### External References
* .copilot-tracking/research/20260113-portfolio-ui-updates-research.md - Detailed implementation plan.

### Standards References
* #file:../../.github/instructions/markdown.instructions.md - Documentation standards.

## Implementation Checklist

### [x] Phase 1: CSS Styling Updates

* [x] Task 1.1: Update Sidebar Styles
  * Details: .copilot-tracking/details/20260113-portfolio-ui-updates-details.md (Lines 10-21)

* [x] Task 1.2: Update Album Card Hover Overlay
  * Details: .copilot-tracking/details/20260113-portfolio-ui-updates-details.md (Lines 23-32)

### [x] Phase 2: Core Logic Refactoring (HTML & JS)

* [x] Task 2.1: Update HTML Template Structure
  * Details: .copilot-tracking/details/20260113-portfolio-ui-updates-details.md (Lines 36-48)

* [x] Task 2.2: Simplify JavaScript Logic
  * Details: .copilot-tracking/details/20260113-portfolio-ui-updates-details.md (Lines 50-64)

## Dependencies

* Python environment for `build.py` (though logic changes are mostly frontend, the template change affects build).
* PhotoSwipe library (already present).

## Success Criteria

* Sidebar scrolls with page and text is centered.
* Hover overlay is wider (80%).
* Clicking albums loads a new page (no hash routing).
* Lightbox works correctly on album pages.
