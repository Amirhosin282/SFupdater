import os
import time
from datetime import datetime, timedelta

def read_settings(settings_path):
    """
    Reads configuration settings from a text file.
    
    Expected file format (line by line):
    1. Number of days (int)
    2. Protected items (comma-separated)
    3. Target folder path (string)
    """
    try:
        with open(settings_path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
            days = int(lines[0])
            protected_items = [p.strip() for p in lines[1].split(",") if p.strip()]
            target_path = lines[2].strip()
            return days, protected_items, target_path
    except Exception as e:
        print(f"[ERROR] Failed to read settings: {e}")
        return None, None, None

def is_old(file_path, days):
    """
    Checks if a file is older than the given number of days.
    """
    try:
        modified_time = os.path.getmtime(file_path)
        return datetime.fromtimestamp(modified_time) < datetime.now() - timedelta(days=days)
    except:
        return False

def clean_folder(base_path, protected_items, days):
    """
    Recursively scans the target folder and deletes:
    - Files older than the specified number of days (unless protected)
    - Empty directories (unless protected)
    """
    for root, dirs, files in os.walk(base_path, topdown=False):
        
        # Delete old files
        for file in files:
            file_path = os.path.join(root, file)
            if any(p in file_path for p in protected_items):
                continue
            if is_old(file_path, days):
                try:
                    os.remove(file_path)
                    print(f"[DELETED FILE] {file_path}")
                except Exception as e:
                    print(f"[ERROR] Could not delete file: {file_path} — {e}")

        # Remove empty directories
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if any(p in dir_path for p in protected_items):
                continue
            try:
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    print(f"[REMOVED EMPTY DIR] {dir_path}")
            except:
                pass

if __name__ == "__main__":
    # Path to settings file (data.txt)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    settings_path = os.path.join(script_dir, "data", "data.txt")

    # Load settings
    days, protected_items, target_path = read_settings(settings_path)

    if days is None or not os.path.exists(target_path):
        print("[ERROR] Invalid settings or target folder not found.")
        time.sleep(2)
        exit()

    # Begin cleaning process
    clean_folder(target_path, protected_items, days)