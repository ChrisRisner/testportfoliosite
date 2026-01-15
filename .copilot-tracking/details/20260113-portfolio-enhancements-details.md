<!-- markdownlint-disable-file -->
# Task Details: Portfolio Site Enhancements

## Research Reference

**Source Research**: [.copilot-tracking/research/20260113-portfolio-enhancements-research.md](.copilot-tracking/research/20260113-portfolio-enhancements-research.md)

## Phase 1: Metadata Generation

### Task 1.1: Create metadata scanning script `src/scan_albums.py`

Create a standalone script to recursively scan the `Albums/` directory and generate a JSON file containing metadata for all images.

* **Files**:
  * Create `src/scan_albums.py`
  * Output `albums_metadata.json` (generated at runtime)
* **Specifications**:
  * Use `PIL.Image` and `PIL.ExifTags` to extract metadata.
  * Schema should match the research proposal: `album_title`, `folder_name`, `photos` list.
  * Extract tags: DateTimeOriginal, Model, LensModel, FocalLength, ISOSpeedRatings, FNumber, ExposureTime.
  * Handle missing tags gracefully.
* **Success**:
  * Running `python src/scan_albums.py` creates a valid JSON file.
* **Research References**:
  * [.copilot-tracking/research/20260113-portfolio-enhancements-research.md](.copilot-tracking/research/20260113-portfolio-enhancements-research.md#L103-L124) (Metadata logic and schema)

## Phase 2: UI & Styling Enhancements

### Task 2.1: Update CSS for navigation and titles

Modify the stylesheet to update navigation link colors and center album titles.

* **Files**:
  * `src/static/style.css`
* **Specifications**:
  * **Nav Links**:
    * Default color: `#999` (Grey).
    * Active/Hover state: `#000000` (Black) and `font-weight: bold` (if desired context implies distinct active state).
  * **Album Titles**:
    * Target the `h2` in the content area.
    * Set `text-align: center`.
* **Success**:
  * Nav links appear grey when inactive and black when active.
  * Album titles are centered.
* **Research References**:
  * [.copilot-tracking/research/20260113-portfolio-enhancements-research.md](.copilot-tracking/research/20260113-portfolio-enhancements-research.md#L72-L82) (CSS Examples)

### Task 2.2: Add social media links to sidebar

Inject social media icons (Instagram, Threads, Email) into the sidebar navigation in the main template.

* **Files**:
  * `src/templates/index.html`
* **Specifications**:
  * Add a container div (e.g., `.social-links`) within the `.sidebar` or below the nav list.
  * Insert the 3 SVG icons provided in research.
  * Ensure SVGs are sized appropriately (width/height 24).
  * Wrap SVGs in anchor tags `<a>` pointing to placeholders (or specific URLs if known, otherwise `#`).
* **Success**:
  * Three icons appear at the bottom of the navigation/sidebar area.
* **Research References**:
  * [.copilot-tracking/research/20260113-portfolio-enhancements-research.md](.copilot-tracking/research/20260113-portfolio-enhancements-research.md#L83-L93) (SVG Assets)

## Phase 3: Performance Optimization

### Task 3.1: Implement smart lazy loading in template

Optimize Largest Contentful Paint (LCP) by eager loading initial images.

* **Files**:
  * `src/templates/index.html`
* **Specifications**:
  * Locate the image iteration loop.
  * Replace static `loading="lazy"` with a conditional Jinja2 expression.
  * Logic: If `loop.index <= 4`, use `loading="eager"`, else `loading="lazy"`.
* **Success**:
  * Generated HTML shows `loading="eager"` for the first 4 images and `lazy` for subsequent ones.
* **Research References**:
  * [.copilot-tracking/research/20260113-portfolio-enhancements-research.md](.copilot-tracking/research/20260113-portfolio-enhancements-research.md#L131-L135) (Lazy loading logic)

## Dependencies

* Python environment with `Pillow` installed.

## Success Criteria

* All UI changes verified visually or via code inspection.
* Metadata script functions without errors.
* Lazy loading attributes are correctly applied in output HTML.
