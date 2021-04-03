import os

def ensure_dir_exists(dir_path: str) -> None:
    """Ensures that a specified directory exists."""
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)