import os
import json
from pathlib import Path
from PIL import Image, ExifTags

ALBUMS_DIR = "Albums"
OUTPUT_FILE = "albums_metadata.json"

# EXIF Tag Mapping
# Using numeric constants or names where available in ExifTags.TAGS
# We'll rely on the tag names provided by PIL where possible, but mapping them to our schema
TAGS_TO_EXTRACT = {
    "DateTimeOriginal": "date_taken",
    "Model": "camera_model",
    "LensModel": "lens_model",
    "FocalLength": "focal_length",
    "ISOSpeedRatings": "iso",
    "FNumber": "aperture",
    "ExposureTime": "shutter_speed"
}

def get_exif_data(image_path):
    exif_data = {}
    try:
        with Image.open(image_path) as img:
            raw_exif = img._getexif()
            if not raw_exif:
                return {}

            for tag_id, value in raw_exif.items():
                tag_name = ExifTags.TAGS.get(tag_id)
                if tag_name in TAGS_TO_EXTRACT:
                    key = TAGS_TO_EXTRACT[tag_name]
                    exif_data[key] = clean_value(key, value)
    except Exception as e:
        print(f"Error reading EXIF for {image_path}: {e}")
    
    return exif_data

def clean_value(key, value):
    """Format EXIF values into readable strings."""
    if key == "focal_length":
        # Tuple (numerator, denominator) or float
        if isinstance(value, tuple) and len(value) == 2:
             if value[1] != 0:
                 return f"{value[0]/value[1]} mm"
        try:
             return f"{float(value)} mm"
        except:
             pass
    
    if key == "aperture":
        if isinstance(value, tuple) and len(value) == 2:
            if value[1] != 0:
                return f"f/{value[0]/value[1]}"
        try:
             return f"f/{float(value)}"
        except:
             pass

    if key == "shutter_speed":
        # Often a tuple (1, 100) -> "1/100"
        if isinstance(value, tuple) and len(value) == 2:
            if value[0] == 1 and value[1] > 1:
                return f"1/{value[1]}s"
            if value[1] != 0:
                val = value[0] / value[1]
                if val < 1 and val > 0:
                     return f"1/{int(1/val)}s"
                return f"{val}s"
        try:
             val = float(value)
             if val < 1 and val > 0:
                 return f"1/{int(1/val)}s"
             return f"{val}s"
        except:
             pass

    if key == "iso":
        # Can be a tuple or int
        if isinstance(value, tuple):
             return value[0]
        return value

    return str(value)

def scan_albums():
    albums_data = {}
    
    if not os.path.exists(ALBUMS_DIR):
        print(f"Directory {ALBUMS_DIR} not found.")
        return

    # Walk through the Albums directory
    # Structure: Albums/<Category>/<Image>
    # Note: Requirements say "recursive scan". Assuming top level folders are albums.
    
    root_path = Path(ALBUMS_DIR)
    
    for album_dir in [d for d in root_path.iterdir() if d.is_dir()]:
        album_name = album_dir.name
        # Skip hidden folders
        if album_name.startswith('.'):
            continue

        print(f"Scanning album: {album_name}")
        
        photos = []
        valid_extensions = {'.jpg', '.jpeg', '.png', '.webp'}
        
        for file in sorted(album_dir.iterdir()):
            if file.suffix.lower() in valid_extensions:
                metadata = get_exif_data(file)
                photos.append({
                    "filename": file.name,
                    "metadata": metadata
                })

        albums_data[album_name] = {
            "album_title": album_name,
            "folder_name": album_name,
            "photos": photos
        }

    with open(OUTPUT_FILE, 'w') as f:
        json.dump(albums_data, f, indent=2)
    
    print(f"Metadata generated in {OUTPUT_FILE}")

if __name__ == "__main__":
    scan_albums()
