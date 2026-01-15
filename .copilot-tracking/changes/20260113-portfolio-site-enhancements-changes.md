<!-- markdownlint-disable-file -->
# Release Changes: Portfolio Site Enhancements

**Related Plan**: 20260113-portfolio-site-enhancements-plan.instructions.md
**Implementation Date**: 2026-01-13

## Summary

Enhancing the portfolio site with improved gallery functionality, responsive design updates, and automated build optimization.

## Changes

### Added

### Modified

* src/templates/index.html - Implemented Jinja2 logic for conditional rendering and updated navigation links.
* src/build.py - Updated build logic to generate individual album pages (SSG) in addition to the home page.
* src/static/style.css - Centered sidebar navigation vertically and refined album card hover styling to be a centered pill overlay.

* src/templates/index.html - Moved the site title into the sidebar for desktop view.
* src/static/style.css - Changed the sidebar background color to white.
* src/static/style.css - Restricted gallery to 2 columns, added global page padding, and added mobile responsive rule for gallery.
* src/static/style.css - Centered the mobile header title and positioned the hamburger menu to the right.
* src/static/app.js - Updated routing logic to show a Home view by default instead of the first album.
* src/static/style.css - Added styles for album cards on the home page.
* src/static/app.js - Implemented renderHome function to display a grid of albums.

### Removed

## Release Summary

**Total Files Affected**: 0

### Files Created (0)

### Files Modified (0)

### Files Removed (0)

### Dependencies & Infrastructure

* **New Dependencies**: None
* **Updated Dependencies**: None
* **Infrastructure Changes**: None
* **Configuration Updates**: None

### Deployment Notes

None
