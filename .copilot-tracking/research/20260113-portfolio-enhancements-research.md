<!-- markdownlint-disable-file -->
# Task Research Documents: Portfolio Enhancements

Research into UI updates for album navigation, title styling, social media integration, image metadata generation, and lazy loading performance improvements.

## Task Implementation Requests
* Change album links in nav to grey (#999).
* Change active album link in nav to black.
* Center album title above image column on album pages.
* Create a pre-build script to scan albums and generate metadata (EXIF, album info).
* Add social links (Instagram, Threads, Email) with SVGs to the bottom of the nav.
* Evaluate lazy loading for off-screen images on album pages.

## Scope and Success Criteria
* Scope: UI styling (`style.css`), Template structure (`index.html`), Build process (`build.py` or new script), Assets (social icons).
* Assumptions: The site is static, built with Python. Images are stored in `Albums/`.
* Success Criteria:
  * Nav links style updates verified.
  * Album title centered.
  * Metadata JSON generation script prototypes.
  * Social links section added with correct SVGs.
  * Lazy loading strategy selected.

## Outline
* Existing Codebase Analysis
* UI/CSS Enhancements
* Metadata Generation Script
* Social Media Integration
* Lazy Loading Strategy
* Recommendations

### Potential Next Research
* **Metadata Utilization**: Research how to update `build.py` to consume the new metadata file for custom covers and titles (as requested for "later").
  * **Reasoning**: The current request only asks for generation, not consumption.
  * **Reference**: User prompt (implied future task).

## Research Executed

### File Analysis
* `src/build.py`: Handles static site generation. Currently scans `Albums/` and processes images on every build. Uses `Pillow` for image manipulation and EXIF extraction.
* `src/templates/index.html`: Jinja2 template. Includes a sidebar for navigation (iterating `db.albums`) and a content area.
* `src/static/style.css`: Controls styling. Includes `.sidebar`, `.nav-list`.

### Code Search Results
* `loading="lazy"` found in `src/templates/index.html` line 41.

## Key Discoveries

### Project Structure
* **Build System**: Single script (`src/build.py`) acting as generator.
* **Navigation**: Generated dynamically in `index.html` from the `albums` list.
* **Album Titles**: Rendered as `<h2>` in the content area.

### Implementation Patterns
* **Image Processing**: `Pillow` library used for resizing and EXIF extraction.
* **Templating**: Jinja2.

### Complete Examples

#### CSS for Nav and Titles
```css
/* Navigation Links */
.nav-link {
    color: #999;
}
.nav-link.active {
    color: #000000;
    font-weight: bold;
}

/* Album Titles */
.content h2 {
    text-align: center;
}
```

#### Social Icons (SVG)
**Instagram**
```html
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
```
**Threads (Standard approximate)**
```html
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"></circle><path d="M16 8v5a3 3 0 0 0 6 0v-1a10 10 0 1 0-3.92 7.94"></path></svg>
```
**Email**
```html
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
```

### API and Schema Documentation

#### Proposed Metadata Schema
```json
{
  "album_title": "Album Name",
  "folder_name": "Folder Name",
  "photos": [
    {
      "filename": "image.jpg",
      "meta": {
        "shutter_speed": "1/125",
        "aperture": "f/2.8",
        "iso": 400,
        "camera_model": "Canon EOS R5",
        "lens_model": "EF 50mm f/1.2L",
        "date_taken": "2023-10-25T14:30:00",
        "focal_length": "50.0 mm"
      }
    }
  ]
}
```

## Technical Scenarios

### 1. Metadata Generation
The user wants a pre-build script. We will extract image scanning logic.
* **Approach**: Create `src/scan_albums.py`.
* **Libraries**: `Pillow` (PIL.ExifTags).
* **Tags to Extract**:
  * DateTimeOriginal (0x9003)
  * Model (0x0110)
  * LensModel (0xA434)
  * FocalLength (0x920A)
  * ISOSpeedRatings (0x8827)
  * FNumber (0x829D)
  * ExposureTime (0x829A)

### 2. Lazy Loading
Current implementation has `loading="lazy"` on all images.
* **Optimization**: Apply conditional loading to improve LCP (Largest Contentful Paint).
* **Logic**: Eager load the first 4 images (above the fold), lazy load the rest.
* **Jinja Implementation**:
```django
<img src="..." loading="{{ 'eager' if loop.index <= 4 else 'lazy' }}" ...>
```

## Recommendations
1.  **Refactor Build Process**: Split "Scanning" into `scan_albums.py` to generate `metadata.json`. Update `build.py` to read this or keep `scan_albums.py` as a generator for the future `db.json`. For now, to satisfy the specific "pre-build script" request, we will create `scan_albums.py` that outputs the JSON, demonstrating the capability.
2.  **UI Updates**: Apply the defined CSS and standard SVGs.
3.  **Performance**: Update `index.html` template loop with the lazy-loading condition.
