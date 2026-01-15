<!-- markdownlint-disable-file -->
# Task Research Documents: Portfolio Site

This research document outlines the architecture for a responsive photography portfolio website. The site will be statically generated using a custom Python script to process images and metadata, hosted on GitHub Pages, and fronted by CloudFlare. The design focuses on a clean two-column layout that adapts to mobile devices, with a high-performance grid gallery and lightbox viewing experience.

## Task Implementation Requests
* Initialize project repository with basic directory structure and necessary setup files (`.gitignore`, `requirements.txt`).
* Implement the Python build script (`build.py`) to scan `Albums/`, extract EXIF metadata, resize images, and generate a `db.json` data file.
* Create the Site Shell HTML/CSS implementing the responsive Two-Column / Hamburger layout.
* Implement the JavaScript logic to fetch `db.json`, render the album grid, and handle navigation.
* Integrate **PhotoSwipe** 5.0 for the lightbox viewing experience within the individual album view.
* Create GitHub Actions workflow for automated building and deployment to GitHub Pages.

## Scope and Success Criteria
* **Scope**: 
    * Entire frontend implementation (HTML/CSS/JS).
    * Backend static generation logic (Python).
    * Deployment configuration (GitHub Actions).
    * Handling of `Albums` folder as the CMS.
* **Assumptions**: 
    * User has basic familiarity with running Python scripts locally for testing.
    * Images provided in `Albums/` are high-resolution JPGs.
    * Source code and images will be hosted in the same repository (ignoring Git LFS for now unless size becomes an issue).
* **Success Criteria**:
    * Running `python build.py` generates a `dist/` folder with a working website.
    * Site passes mobile responsiveness checks (Hamburger menu appears on small screens).
    * Keyboard navigation works in the Lightbox view.
    * EXIF data (Aperture, Shutter) is extracted and available in the data model.

## Outline
* **Project Structure**: Convention for file organization.
* **Architecture**: Python Generator + Vanilla JS Frontend.
* **Data Model**: Schema for `db.json` and `metadata.json`.
* **Technical Scenarios**:
    * Layout Strategy (CSS Grid).
    * Image Processing Pipeline.
    * Deployment Workflow.

### Potential Next Research
* **Lazy Loading Strategy**: Research native `loading="lazy"` vs JS intersection observer for the grid to improve performance with large albums.
    * **Reasoning**: Large photo albums can hurt initial load time.
    * **Reference**: General web performance best practices.
* **Search Functionality**: A client-side search based on metadata keywords.
    * **Reasoning**: As the portfolio grows, finding specific types of shots might be useful.
    * **Reference**: User request mentioned "metadata file... that we might later display".

## Research Executed

### File Analysis
* `/Users/chrisner/code/portfoliosite2/Albums/`:
    * Found existing structure `Food/` and `Portugal/`.
    * Confirms filesystem-based content management is the correct path.

### External Research (Evidence Log)
* **Subagent Research**: `Deep Analysis of Portfolio Requirements`
    * Confirmed **PhotoSwipe** as the best candidate for "dependency-free lightbox with keyboard nav".
    * Validated **Python + Pillow** as the most flexible approach for the "scripts to handle generating new albums" requirement over standard SSGs.
    * Source: Internal Subagent Analysis (2026-01-13).

### Project Conventions
* **Instructions followed**: 
    * `.github/instructions/python-script.instructions.md` (Will be applied to `build.py`).
    * `.github/instructions/markdown.instructions.md`.

## Key Discoveries

### Project Structure
The project will follow a strict separation of "Content" (Albums) and "Code" (Src).

```text
/
├── Albums/                 # The "Database"
│   ├── Food/
│   │   ├── _cover.jpg      # Optional manual cover override
│   │   ├── metadata.json   # Optional metadata
│   │   └── img1.jpg
│   └── Portugal/
├── src/                    # Source Code
│   ├── static/             # Assets (CSS, JS, Icons)
│   ├── templates/          # HTML Templates (Jinja2)
│   └── build.py            # Static Site Generator
├── dist/                   # Build Output (GitIgnored)
└── requirements.txt        # Python dependencies
```

### Implementation Patterns
* **Static Generation**: We will not use a runtime framework (React/Next). We will generate a single-page-application feel or distinct HTML pages using a "Database File" (`db.json`) approach. 
    * *Decision*: generating static HTML files for SEO (one `index.html` per album) is actionable via Python, but loading a single JSON blob is smoother for the user experience. Given the requirement for "Clicking the photo should open the same type of two column view... with the same navigation", a Single Page App (SPA) feel using Vanilla JS and History API is efficient, but Static HTML Files are more robust for straightforward hosting. 
    * *Refined Decision*: **Hybrid**. The Python script will generate:
        1. `index.html` (The landing page).
        2. `album/[slug]/index.html` (Per-album pages for deep linking/SEO).
        3. A shared `data.js` or `db.json` payload so transitions can be instant if we choose to enhance with JS.

### Complete Examples

**Metadata Schema (`Albums/Portugal/metadata.json`)**
```json
{
  "title": "Portugal Trip",
  "date": "2025-12-01",
  "description": "Walking the streets of Lisbon.",
  "cover_image": "IMG_001.jpg", 
  "sort_order": "chronological"
}
```

**Data Model (Generated `db.json`)**
```json
{
  "albums": [
    {
      "slug": "portugal",
      "title": "Portugal Trip",
      "cover": "/media/portugal/thumb_IMG_001.jpg",
      "photos": [
        {
          "src": "/media/portugal/large_IMG_001.jpg",
          "w": 1200,
          "h": 800,
          "meta": {
            "shutter": "1/200",
            "aperture": "f/2.8"
          }
        }
      ]
    }
  ]
}
```

## Technical Scenarios

### 1. The Responsive Layout Engine
**Requirements:**
* Two columns on Desktop (Nav | Grid).
* Single column on Mobile (Hamburger | Grid).
* Nav stays fixed or sticky on Desktop.

**Preferred Approach:** CSS Grid
* The main container will use CSS Grid.
* Media Query (`@media (max-width: 768px)`) triggers the layout shift.

```css
/* structure.css */
.container {
    display: grid;
    grid-template-columns: 250px 1fr; /* Sidebar fixed width, Content fills rest */
    min-height: 100vh;
}

@media (max-width: 768px) {
    .container {
        display: block; /* Stacked */
    }
    .sidebar {
        display: none; /* Hidden, triggered by hamburger */
    }
    .hamburger-header {
        display: flex; /* Visible */
    }
}
```

### 2. Image Processing & Metadata Extraction (The Build Script)
**Requirements:**
* Process `Albums/` folder.
* Resize images for web (thumbnails for grid, larger optimized for lightbox).
* Extract EXIF.

**Preferred Approach:** Python `build.py`
Use `os.walk` to traverse `Albums`. Use `PIL` (Pillow) to open images.

```python
# build.py snippet
from PIL import Image, ExifTags

def get_exif(img_path):
    img = Image.open(img_path)
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    return {
        "shutter": exif.get("ExposureTime"),
        "aperture": exif.get("FNumber"),
        "iso": exif.get("ISOSpeedRatings")
    }
```

#### Considered Alternatives
* **JavaScript (Node.js)**: Good, but Python is often cleaner for standalone scripts and has excellent image libraries without native compilation issues.
* **Client-side generation**: Too slow to parse EXIF in browser for every visit.

### 3. Lightbox Integration
**Requirements:**
* Keyboard nav.
* Metadata display capability.

**Preferred Approach:** PhotoSwipe 5 (CDN ES Module)
To maintain a "zero-maintenance" philosophy, we will avoid complex bundlers (Webpack/Vite) and use native ES Modules loaded via CDN.

**Implementation Details:**
We will use an Import Map or direct imports to load PhotoSwipe without a build step.

**HTML Snippet:**
```html
<link rel="stylesheet" href="https://unpkg.com/photoswipe@5.4.3/dist/photoswipe.css">

<script type="module">
  import PhotoSwipeLightbox from 'https://unpkg.com/photoswipe@5.4.3/dist/photoswipe-lightbox.esm.js';
  import PhotoSwipe from 'https://unpkg.com/photoswipe@5.4.3/dist/photoswipe.esm.js';

  const lightbox = new PhotoSwipeLightbox({
    gallery: '#gallery--getting-started',
    children: 'a',
    pswpModule: PhotoSwipe
  });
  lightbox.init();
</script>
```

### 4. GitHub Actions Workflow
**Requirements:**
* Automated build on push to main.
* Deploy to GitHub Pages.

**Preferred Approach:** Standard `actions/deploy-pages`
We will use the official actions for setting up Pages. The workflow will run the python generator and upload the `dist/` folder.

**Workflow Snippet (.github/workflows/deploy.yml):**
```yaml
name: Deploy Portfolio

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'
          
      - name: Install Dependencies
        run: pip install -r requirements.txt
        
      - name: Build Site
        run: python src/build.py
        
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: './dist'

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

