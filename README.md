# Portfolio Site

A static portfolio site generator that turns a directory of images into a responsive, single-page photo gallery.

## Features

*   **Static Generation**: Python script processes images and generates a lightweight static site.
*   **Responsive Design**: CSS Grid layout with a fixed sidebar on desktop and a hamburger menu on mobile.
*   **Lightbox**: Integrated PhotoSwipe 5.0 for full-screen image viewing with keyboard support.
*   **Content Management**: Simply add folders and images to the `Albums/` directory.

## Architecture

*   **Backend (Build)**: `src/build.py` uses Pillow to resize images, extract EXIF metadata, and generates `dist/db.json` and `dist/index.html` using Jinja2.
*   **Frontend**: Vanilla JavaScript (`src/static/app.js`) fetches the JSON data and renders the album grid client-side. Routing is handled via URL hash.

## Prerequisites

*   Python 3.11+

## Installation

1.  Clone the repository.
2.  Create a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Content Management

1.  Create a folder in `Albums/` for each album (e.g., `Albums/Travel`).
2.  Add `.jpg`, `.png`, or `.webp` images to the folder.
3.  The folder name will become the album title.

## Metadata Generation

To extract EXIF metadata (camera model, lens, exposure settings) from your images and generate a `albums_metadata.json` file:

```bash
python src/scan_albums.py
```

## Building the Site

To generate the site artifacts in the `dist/` directory:

```bash
python src/build.py
```

## Running Locally

To preview the site locally, you can serve the `dist` directory using Python's built-in HTTP server:

```bash
# Ensure you have built the site first
python src/build.py

# Serve the dist directory
cd dist
python -m http.server 8000
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

## Deployment

The project is configured for automated deployment to GitHub Pages via GitHub Actions.
Any push to the `main` branch will trigger a build and deploy the content of `dist/` to the `gh-pages` environment.
