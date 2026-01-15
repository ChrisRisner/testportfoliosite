<!-- markdownlint-disable-file -->
# Task Details: Portfolio Site Implementation

## Research Reference

**Source Research**: .copilot-tracking/research/20260113-portfolio-site-research.md

## Phase 1: Project Initialization & Build System

### Task 1.1: Initialize Project Structure & Dependencies

Set up the directory structure as defined in the research and create the requirements file for the build script.

* **Files**:
  * `src/build.py` - Empty placeholder or initial setup
  * `src/static/` - Directory for CSS/JS assets
  * `src/templates/` - Directory for HTML templates
  * `requirements.txt` - Python dependencies
* **Success**:
  * Directory structure matches Research Lines 73-86
  * `requirements.txt` contains `Pillow` and `Jinja2` (if needed) or just standard libs found in research.
* **Research References**:
  * .copilot-tracking/research/20260113-portfolio-site-research.md (Lines 73-86) - Project Structure
* **Dependencies**:
  * None

### Task 1.2: Implement Python Build Script (Metadata & Image Processing)

Create the `build.py` script to walk the `Albums/` directory, process images (resize/optimize), extract EXIF data, and generate `dist/db.json` and `dist/index.html`.

* **Files**:
  * `src/build.py` - Main build logic
  * `src/templates/index.html` - Base Jinja2 template
* **Success**:
  * Script runs without errors
  * `dist/` folder is created
  * `dist/db.json` matches schema in Research Lines 98-124
  * Images are resized and placed in `dist/media/`
* **Research References**:
  * .copilot-tracking/research/20260113-portfolio-site-research.md (Lines 152-168) - Image Processing & Metadata Extraction
* **Dependencies**:
  * Task 1.1 completion

## Phase 2: Frontend Implementation

### Task 2.1: Site Shell & Responsive Layout

Create the main CSS and HTML structure to support the two-column desktop layout and hamburger mobile layout.

* **Files**:
  * `src/static/style.css` - CSS Grid and Media Queries
  * `src/templates/index.html` - Updated HTML structure
* **Success**:
  * Desktop: Fixed sidebar (250px), fluid content
  * Mobile: Hidden sidebar, visible hamburger header
* **Research References**:
  * .copilot-tracking/research/20260113-portfolio-site-research.md (Lines 134-149) - Responsive Layout Engine
* **Dependencies**:
  * Phase 1 completion

### Task 2.2: JavaScript Logic & Data Rendering

Implement client-side JS to fetch `db.json` and dynamically render the available albums and photos into the grid.

* **Files**:
  * `src/static/app.js` - Application logic
* **Success**:
  * Navigation updates based on current album
  * Grid displays photos from `db.json`
* **Research References**:
  * .copilot-tracking/research/20260113-portfolio-site-research.md (Lines 88-100) - Data Model usage
* **Dependencies**:
  * Task 2.1 completion

### Task 2.3: Integrate PhotoSwipe Lightbox

Add PhotoSwipe via CDN and initialize it on the grid items.

* **Files**:
  * `src/templates/index.html` - Add CDN links
  * `src/static/app.js` - Initialize PhotoSwipeLightbox
* **Success**:
  * Clicking an image opens it in full screen
  * Keyboard navigation (Left/Right) works
* **Research References**:
  * .copilot-tracking/research/20260113-portfolio-site-research.md (Lines 171-193) - Lightbox Integration
* **Dependencies**:
  * Task 2.2 completion

## Phase 3: Deployment Configuration

### Task 3.1: GitHub Actions Workflow

Create the workflow file to build and deploy the site to GitHub Pages.

* **Files**:
  * `.github/workflows/deploy.yml` - Workflow configuration
* **Success**:
  * Workflow triggers on push to main
  * `python src/build.py` executes successfully
  * Artifact uploaded and deployed to Pages
* **Research References**:
  * .copilot-tracking/research/20260113-portfolio-site-research.md (Lines 200-244) - GitHub Actions Workflow
* **Dependencies**:
  * Phase 2 completion

## Dependencies

* Python 3
* Node.js (Optional for testing, strictly Python implementation planned)

## Success Criteria

* Fully functional static site generated in `dist/`
* Responsive design verified at mobile and desktop breakpoints
