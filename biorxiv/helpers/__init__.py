import sys
import os
from pathlib import Path

def generate_download_path() -> Path:
    home = Path.home()
    dirname = "biorxiv_articles"
    if dirname not in os.listdir(home):
        os.mkdir(home / dirname)


PLATFORM = sys.platform
HOME = os.path.expanduser("~")
DIRNAME = "biorxiv_articles"

if DIRNAME not in os.listdir(HOME):
    os.mkdir(DIRNAME)

DOWNLOAD_PATH = Path(HOME) / Path(DIRNAME)


def download_article(url: str, path: Path=DOWNLOAD_PATH) -> bool:
    """
    Downloads a full article in pdf format to `path`.
    If `path` is not provided, article is saved at a path stored in the 
    $HOME variable within a directory named `biorxiv_arciles`.
    """
