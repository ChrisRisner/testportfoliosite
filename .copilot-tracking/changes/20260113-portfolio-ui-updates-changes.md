<!-- markdownlint-disable-file -->
# Release Changes: Portfolio UI Updates

**Related Plan**: .copilot-tracking/plans/20260113-portfolio-ui-updates-plan.instructions.md
**Implementation Date**: 2026-01-13

## Summary

This release implements UI updates for the portfolio site, specifically focusing on adding a contact section and improving the gallery layout.

## Changes

### Added

### Modified

* src/static/style.css - Updated sidebar to remove sticky positioning and center text.
* src/static/style.css - Increased album card hover overlay width to 80%.
* src/templates/index.html - Removed data injection, updated gallery to use standard anchors, updated script tag.
* src/static/app.js - Removed SPA routing logic, simplified to PhotoSwipe initialization and mobile menu toggle.

* src/static/style.css - Refactored layout to use centered flexbox, updated album thumbnails to square aspect ratio with full-cover hover effects.
* src/build.py - Added `ImageOps.exif_transpose` to respect EXIF orientation tags, and implemented photo pairing logic.

### Removed

## Release Summary

**Total Files Affected**: 1

### Files Created (0)

### Files Modified (2)

* src/static/style.css - Refactored layout and updated album thumbnails.
* src/build.py - Added EXIF support and photo ordering logic.

* src/static/style.css - Updated padding, aspect ratios, and 

### Dependencies & Infrastructure

* **New Dependencies**: None
* **Updated Dependencies**: None
* **Infrastructure Changes**: None
* **Configuration Updates**: None

### Deployment Notes

None
