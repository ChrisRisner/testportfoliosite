#!/usr/bin/env python3
"""
Check author information in all album images.
Usage: python check_authors.py
"""

import os
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS, IFD

def get_author_info(image_path):
    """Extract author-related metadata from an image."""
    author_info = {
        "artist": None,
        "copyright": None,
        "creator": None,
        "author": None
    }
    
    try:
        with Image.open(image_path) as img:
            exif = img.getexif()
            
            if not exif:
                return author_info
            
            # Check standard EXIF tags
            for tag_id, value in exif.items():
                tag_name = TAGS.get(tag_id, tag_id)
                
                if tag_name == "Artist":
                    author_info["artist"] = value
                elif tag_name == "Copyright":
                    author_info["copyright"] = value
                elif tag_name == "Author":
                    author_info["author"] = value
            
            # Check XMP/IPTC data in EXIF IFD if available
            try:
                ifd = exif.get_ifd(IFD.Exif)
                if ifd:
                    for tag_id, value in ifd.items():
                        tag_name = TAGS.get(tag_id, tag_id)
                        if tag_name == "Artist":
                            author_info["artist"] = value
            except:
                pass
                
    except Exception as e:
        return {"error": str(e)}
    
    return author_info

def check_albums(albums_dir="Albums"):
    """Scan all albums and report author information."""
    
    if not os.path.exists(albums_dir):
        print(f"Error: Directory '{albums_dir}' not found.")
        return
    
    root_path = Path(albums_dir)
    total_images = 0
    images_with_author = 0
    images_without_author = 0
    errors = 0
    
    # Valid image extensions
    valid_extensions = {'.jpg', '.jpeg', '.png', '.webp'}
    
    print("=" * 80)
    print("IMAGE AUTHOR INFORMATION CHECK")
    print("=" * 80)
    print()
    
    # Scan each album
    for album_dir in sorted(root_path.iterdir()):
        if not album_dir.is_dir() or album_dir.name.startswith('.'):
            continue
        
        print(f"\n📁 ALBUM: {album_dir.name}")
        print("-" * 80)
        
        album_images = []
        
        # Collect all images in this album
        for file in sorted(album_dir.iterdir()):
            if file.suffix.lower() in valid_extensions:
                album_images.append(file)
        
        if not album_images:
            print("  (no images found)")
            continue
        
        # Check each image
        for file in album_images:
            total_images += 1
            author_info = get_author_info(file)
            
            if "error" in author_info:
                errors += 1
                print(f"  ❌ {file.name}")
                print(f"     ERROR: {author_info['error']}")
                continue
            
            # Check if any author field is populated
            has_author = any([
                author_info.get("artist"),
                author_info.get("copyright"),
                author_info.get("author")
            ])
            
            if has_author:
                images_with_author += 1
                print(f"  ✓ {file.name}")
                if author_info.get("artist"):
                    print(f"     Artist: {author_info['artist']}")
                if author_info.get("copyright"):
                    print(f"     Copyright: {author_info['copyright']}")
                if author_info.get("author"):
                    print(f"     Author: {author_info['author']}")
            else:
                images_without_author += 1
                print(f"  ✗ {file.name}")
                print(f"     No author information found")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total images checked: {total_images}")
    print(f"Images WITH author info: {images_with_author} ({images_with_author/total_images*100:.1f}%)" if total_images > 0 else "Images WITH author info: 0")
    print(f"Images WITHOUT author info: {images_without_author} ({images_without_author/total_images*100:.1f}%)" if total_images > 0 else "Images WITHOUT author info: 0")
    if errors > 0:
        print(f"Errors encountered: {errors}")
    print()

if __name__ == "__main__":
    check_albums()