*--
applyTo: '.copilot-tracking/changes/20260113-portfolio-site-changes.md'
*--
<!-- markdownlint-disable-file -->
# Task Checklist: Portfolio Site Implementation

## Overview

Implement a static portfolio site using Python for build-time generation and Vanilla JS for the frontend, featuring a responsive two-column layout and PhotoSwipe lightbox.

Follow all instructions from #file:../../.github/instructions/task-implementation.instructions.md

## Objectives

* Create a Python build script to process images and generate site data
* Implement a responsive two-column layout (Desktop) / hamburger menu (Mobile)
* Integrate PhotoSwipe 5.0 for image viewing with keyboard navigation
* Configure GitHub Actions for automated deployment to GitHub Pages

## Research Summary

### Project Files
* Albums/ - Existing content directory acting as the CMS
* src/ - Target directory for source code

### External References
* .copilot-tracking/research/20260113-portfolio-site-research.md - Portfolio Site Architecture and Requirements
* "PhotoSwipe 5 Documentation" - Lightbox implementation pattern

### Standards References
* #file:../../.github/instructions/python-script.instructions.md - Python scripting conventions
* #file:../../.github/instructions/bicep/bicep.instructions.md - Not used, but standard reference

## Implementation Checklist

### [x] Phase 1: Project Initialization & Build System

* [x] Task 1.1: Initialize Project Structure & Dependencies
  * Details: .copilot-tracking/details/20260113-portfolio-site-details.md (Lines 11-20)

* [x] Task 1.2: Implement Python Build Script (Metadata & Image Processing)
  * Details: .copilot-tracking/details/20260113-portfolio-site-details.md (Lines 22-38)

### [x] Phase 2: Frontend Implementation

* [x] Task 2.1: Site Shell & Responsive Layout
  * Details: .copilot-tracking/details/20260113-portfolio-site-details.md (Lines 42-53)

* [x] Task 2.2: JavaScript Logic & Data Rendering
  * Details: .copilot-tracking/details/20260113-portfolio-site-details.md (Lines 55-65)

* [x] Task 2.3: Integrate PhotoSwipe Lightbox
  * Details: .copilot-tracking/details/20260113-portfolio-site-details.md (Lines 67-78)

### [x] Phase 3: Deployment Configuration

* [x] Task 3.1: GitHub Actions Workflow
  * Details: .copilot-tracking/details/20260113-portfolio-site-details.md (Lines 82-92)

## Dependencies

* Python 3.11+
* Pillow (Python Image Library)
* PhotoSwipe 5.0 (CDN)

## Success Criteria

* `python src/build.py` successfully generates `dist/` with `index.html` and processed images
* Site displays two columns on desktop and hamburger menu on mobile
* Images open in Lightbox with keyboard support
* GitHub Actions workflow passes and deploys to Pages
