---
applyTo: '.copilot-tracking/changes/20260113-portfolio-enhancements-changes.md'
---
<!-- markdownlint-disable-file -->
# Task Checklist: Portfolio Site Enhancements

## Overview

Implement UI refinements, social media integration, performance optimizations, and a metadata generation script for the portfolio site.

Follow all instructions from [Task Implementation Instructions](.github/instructions/task-implementation.instructions.md).

## Objectives

* Center album titles and update navigation link styling (grey inactive, black active).
* Add Instagram, Threads, and Email social icons to the navigation sidebar.
* Implement a conditional lazy loading strategy for album images.
* Create a Python script to scan albums and generate EXIF metadata.

## Research Summary

### Project Files
* [src/build.py](src/build.py) - Current build script handling static generation.
* [src/templates/index.html](src/templates/index.html) - Main template requiring social links and lazy loading logic.
* [src/static/style.css](src/static/style.css) - Stylesheet for nav and title updates.

### External References
* [.copilot-tracking/research/20260113-portfolio-enhancements-research.md](.copilot-tracking/research/20260113-portfolio-enhancements-research.md) - Verified requirements and SVG assets.

## Implementation Checklist

### [x] Phase 1: Metadata Generation

* [x] Task 1.1: Create metadata scanning script `src/scan_albums.py`.
  * Details: [.copilot-tracking/details/20260113-portfolio-enhancements-details.md](.copilot-tracking/details/20260113-portfolio-enhancements-details.md#L10)

### [x] Phase 2: UI & Styling Enhancements

* [x] Task 2.1: Update CSS for navigation and titles.
  * Details: [.copilot-tracking/details/20260113-portfolio-enhancements-details.md](.copilot-tracking/details/20260113-portfolio-enhancements-details.md#L30)

* [x] Task 2.2: Add social media links to sidebar.
  * Details: [.copilot-tracking/details/20260113-portfolio-enhancements-details.md](.copilot-tracking/details/20260113-portfolio-enhancements-details.md#L45)

### [x] Phase 3: Performance Optimization

* [x] Task 3.1: Implement smart lazy loading in template.
  * Details: [.copilot-tracking/details/20260113-portfolio-enhancements-details.md](.copilot-tracking/details/20260113-portfolio-enhancements-details.md#L65)

## Dependencies

* Python `Pillow` library for EXIF extraction.

## Success Criteria

* `src/scan_albums.py` successfully generates `albums_metadata.json` with EXIF data.
* Navigation links are grey (#999) by default and black/bold when active.
* Album titles are centered on the page.
* Social icons appear correctly in the sidebar.
* First 4 images on album pages load eagerly; subsequent images load lazily.
