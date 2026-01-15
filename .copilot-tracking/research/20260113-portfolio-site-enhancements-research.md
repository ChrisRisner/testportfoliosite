# Research: Portfolio Site Enhancements

**Date:** 2026-01-13
**Author:** GitHub Copilot
**Status:** In Progress
**Related Files:** `src/build.py`, `src/static/style.css`, `src/templates/index.html`

## Scope
The goal is to enhance the portfolio site by refining the UI and shifting from a JS-heavy SPA approach to a multi-page static site generation architecture.

## Success Criteria
1.  **Centered Navigation:** The navigation menu in the sidebar should be visually centered or aligned according to design requirements (user specified "Center nav").
2.  **Fix Hover Padding:** Adjust the album card hover effect (white box) to look better, likely by adjusting padding or positioning.
3.  **Per-Album Pages:** The build script must generate individual HTML pages for each album (e.g., `/portugal/index.html`) instead of relying solely on client-side JavaScript injection.

## Findings

### CSS Selectors
*   **Navigation Alignment:**
    *   Container: `.sidebar` (currently `flex-shrink: 0`, fixed width).
    *   List: `.nav-list`.
    *   To center the nav vertically within the sidebar, we can add `display: flex; flex-direction: column; justify-content: center;` to `.sidebar`.
*   **Album Hover Effect:**
    *   Selector: `.album-card h3`.
    *   Current Style: `background: rgba(255, 255, 255, 0.9);`. It covers the whole card (`width: 100%; height: 100%;`).
    *   Problem: It covers the entire image.
    *   Potential Fix: Make it a smaller box, or a bar at the bottom, or adjust padding/margin.

### Template Structure (`src/templates/index.html`)
*   Current Layout: Sidebar + Empty `<main id="content">`.
*   Data: Full DB injected via `window.portfolioData`.
*   Logic: Client-side rendering via `app.js`.

### Build Script (`src/build.py`)
*   Iterates `Albums/` directory.
*   Processes images (resize, metadata).
*   Generates `db.json`.
*   Renders a *single* `index.html` using the `db` context.

## Technical Scenarios: Generating Per-Album Pages

### Scenario A: Reuse `index.html` (Recommended)
We can reuse the existing template structure but inject specific context for the active album.

**Changes Required:**
1.  **Template:** Update `index.html` to accept an optional `active_album` variable.
    *   If `active_album` is present, render the photo grid server-side inside `main`.
    *   If `active_album` is None (Home), render the list of albums (Gallery view).
2.  **Build Script:**
    *   Loop through `albums_data`.
    *   Create a directory `dist/<slug>/`.
    *   Render `index.html` with `active_album=album` and `db=db`.
    *   Save to `dist/<slug>/index.html`.
    *   Render the root `dist/index.html` (Home).

### Scenario B: Separate Templates
Create `album.html` specifically for album pages.
*   Pros: Cleaner separation if layouts diverge significantly.
*   Cons: Code duplication (sidebar, header).

*Decision:* Scenario A is sufficient for now as the layout is shared.

## Implementation Plan

### 1. Modify `src/build.py`
We need to change the generation phase at the end of `main()`.

**Current Code:**
```python
    # Generate HTML
    if (TEMPLATE_DIR / "index.html").exists():
        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        template = env.get_template("index.html")
        output_html = template.render(db=db)
        
        with open(DIST_DIR / "index.html", "w") as f:
            f.write(output_html)
```

**Proposed Change:**
```python
    # Generate Pages
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template("index.html")

    # 1. Generate Home Page (Root)
    home_html = template.render(db=db, current_album=None)
    with open(DIST_DIR / "index.html", "w") as f:
        f.write(home_html)

    # 2. Generate Album Pages
    for album in albums_data:
        album_slug = album["slug"]
        album_dir = DIST_DIR / album_slug
        album_dir.mkdir(exist_ok=True)
        
        # Adjust photo paths if necessary (relative vs absolute)
        # Assuming photo.src starts with "/" (e.g., /media/...), it should work fine.
        
        album_html = template.render(db=db, current_album=album)
        with open(album_dir / "index.html", "w") as f:
            f.write(album_html)
```

### 2. Update `src/templates/index.html`
Add server-side rendering logic to the `<main>` block.

```html
<main class="content" id="content">
    {% if current_album %}
        <h2>{{ current_album.title }}</h2>
        <div class="album-grid">
            {% for photo in current_album.photos %}
            <div class="photo-link">
                <!-- Use photoSwipe HTML structure if needed here, or just images -->
                <img class="photo-item" src="{{ photo.src }}" 
                     data-pswp-src="{{ photo.src }}"
                     data-pswp-width="{{ photo.w }}" 
                     data-pswp-height="{{ photo.h }}" 
                     alt="" loading="lazy">
            </div>
            {% endfor %}
        </div>
    {% else %}
        <!-- Home View: List of Albums -->
        <div class="album-grid">
            {% for album in db.albums %}
            <a href="/{{ album.slug }}/" class="album-card">
                <img src="{{ album.cover }}" alt="{{ album.title }}">
                <h3>{{ album.title }}</h3>
            </a>
            {% endfor %}
        </div>
    {% endif %}
</main>
```

### 3. CSS Adjustments
*   Center the sidebar navigation content.
*   Refine the `.album-card h3` style.
