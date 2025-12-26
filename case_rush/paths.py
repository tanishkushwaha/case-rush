"""
Defines and creates paths for data, config and export directories.
"""

from pathlib import Path
from platformdirs import user_data_dir, user_config_dir, user_cache_dir

APP_NAME = "case-rush"

DATA_DIR = Path(user_data_dir(APP_NAME))
CONFIG_DIR = Path(user_config_dir(APP_NAME))
CACHE_DIR = Path(user_cache_dir(APP_NAME))

EXPORT_DIR = DATA_DIR / "export"
ITEMS_DIR = DATA_DIR / "items"

DATA_DIR.mkdir(parents=True, exist_ok=True)
CONFIG_DIR.mkdir(parents=True, exist_ok=True)
EXPORT_DIR.mkdir(parents=True, exist_ok=True)
CACHE_DIR.mkdir(parents=True, exist_ok=True)


for letter in "SABCD":
    (ITEMS_DIR / letter).mkdir(parents=True, exist_ok=True)
