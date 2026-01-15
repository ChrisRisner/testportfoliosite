#!/usr/bin/env python3
"""
Portfolio Site Builder
Generates static site from content in Albums/ directory.
"""

import os
import sys
import json
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional

from PIL import Image, ExifTags, ImageOps
from jinja2 import Environment, FileSystemLoader

# Configuration
ALBUMS_DIR = Path("Albums")
DIST_DIR = Path("dist")
MEDIA_DIR = DIST_DIR / "media"
TEMPLATE_DIR = Path("src/templates")
STATIC_DIR = Path("src/static")

# Base URL configuration
BASE_URL = os.getenv("SITE_BASE_URL", "")

LARGE_SIZE = (1600, 1200)
THUMB_SIZE = (600, 600)

def setup_directories():
    """Ensure output directories exist."""
    print("Setting up directories...")
    MEDIA_DIR.mkdir(parents=True, exist_ok=True)
    
    # Copy static assets if they exist
    if STATIC_DIR.exists():
        dist_static = DIST_DIR / "static"
        if dist_static.exists():
            shutil.rmtree(dist_static)
        shutil.copytree(STATIC_DIR, dist_static)

def get_exif_data(img: Image.Image) -> Dict[str, str]:
    """Extract and format specific EXIF data."""
    meta = {}
    exif = img.getexif()
    if not exif:
        return meta
        
    for key, val in exif.items():
        if key in ExifTags.TAGS:
            tag = ExifTags.TAGS[key]
            if tag == "ExposureTime":
                # Convert fraction if needed, simplistically for now
                meta["shutter"] = str(val)
            elif tag == "FNumber":
                meta["aperture"] = f"f/{float(val):.1f}"
            elif tag == "ISOSpeedRatings":
                meta["iso"] = str(val)
    return meta

def process_image(img_path: Path, album_slug: str) -> Optional[Dict[str, Any]]:
    """Process a single image."""
    try:
        filename = img_path.name
        slug_dir = MEDIA_DIR / album_slug
        slug_dir.mkdir(exist_ok=True)
        
        large_filename = f"large_{filename}"
        thumb_filename = f"thumb_{filename}"
        
        large_path = slug_dir / large_filename
        thumb_path = slug_dir / thumb_filename
        
        with Image.open(img_path) as img:
            # Handle orientation if needed (Exif transpose)
            img = ImageOps.exif_transpose(img)
            
            # Extract Meta
            meta = get_exif_data(img)
            
            # Save Large
            img_large = img.copy()
            img_large.thumbnail(LARGE_SIZE)
            img_large.save(large_path, quality=85)
            
            # Save Thumb
            img_thumb = img.copy()
            img_thumb.thumbnail(THUMB_SIZE)
            img_thumb.save(thumb_path, quality=80)
            
            width, height = img_large.size
            
            return {
                "src": f"/media/{album_slug}/{large_filename}",
                "w": width,
                "h": height,
                "meta": meta,
                "thumb": f"/media/{album_slug}/{thumb_filename}"
            }
    except Exception as e:
        print(f"Error processing {img_path}: {e}")
        return None

def optimize_photo_order(photos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Reorder photos to pair portraits together for better grid layout.
    """
    portraits = []
    landscapes = []
    
    for p in photos:
        w, h = p.get('w', 1), p.get('h', 1)
        ratio = w / h if h else 1.0
        
        if ratio < 0.85: # Clear portrait
            portraits.append(p)
        else:
            landscapes.append(p)
            
    # Create final list pairs
    ordered = []
    
    # Add pairs of portraits
    for i in range(0, len(portraits), 2):
        if i + 1 < len(portraits):
            ordered.extend([portraits[i], portraits[i+1]])
        else:
            ordered.append(portraits[i]) # Orphan portrait
            
    # Add landscapes
    ordered.extend(landscapes)
    
    return ordered

def main() -> int:
    """Main build entry point."""
    print("Starting build process...")
    setup_directories()
    
    albums_data = []

    if not ALBUMS_DIR.exists():
        print(f"Error: {ALBUMS_DIR} not found.")
        return 1

    for album_path in sorted(ALBUMS_DIR.iterdir()):
        if not album_path.is_dir() or album_path.name.startswith('.'):
            continue
            
        album_slug = album_path.name.lower().replace(" ", "-")
        print(f"Processing Album: {album_path.name}")
        
        photos = []
        valid_extensions = {".jpg", ".jpeg", ".png", ".webp", ".JPG", ".JPEG"}
        
        for img_path in sorted(album_path.iterdir()):
            if img_path.suffix in valid_extensions:
                photo_data = process_image(img_path, album_slug)
                if photo_data:
                    photos.append(photo_data)
        
        # Optimize order
        photos = optimize_photo_order(photos)
        
        if photos:
            albums_data.append({
                "slug": album_slug,
                "title": album_path.name,
                "cover": photos[0]["thumb"],
                "photos": photos
            })
    
    db = {"albums": albums_data}
    
    # Save DB
    with open(DIST_DIR / "db.json", "w") as f:
        json.dump(db, f, indent=2)
    print(f"Database generated with {len(albums_data)} albums.")
        
    # Generate HTML
    if (TEMPLATE_DIR / "index.html").exists():
        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        template = env.get_template("index.html")
        
        # 1. Generate Home Page
        print("Generating Home Page...")
        home_html = template.render(db=db, current_album=None, base_url=BASE_URL)
        with open(DIST_DIR / "index.html", "w") as f:
            f.write(home_html)
            
        # 2. Generate Album Pages
        print("Generating Album Pages...")
        for album in albums_data:
            slug = album["slug"]
            album_dir = DIST_DIR / slug
            album_dir.mkdir(exist_ok=True, parents=True)
            
            album_html = template.render(db=db, current_album=album, base_url=BASE_URL)
            with open(album_dir / "index.html", "w") as f:
                f.write(album_html)
                
        print(f"Generated home and {len(albums_data)} album pages.")

        # 3. Generate 404 Page
        print("Generating 404 Page...")
        if (TEMPLATE_DIR / "404.html").exists():
            template_404 = env.get_template("404.html")
            html_404 = template_404.render(db=db, base_url=BASE_URL)
            with open(DIST_DIR / "404.html", "w") as f:
                f.write(html_404)
        else:
            print("Warning: 404.html template not found.")

    else:
        print("Warning: index.html template not found.")

    return 0

if __name__ == "__main__":
    sys.exit(main())
