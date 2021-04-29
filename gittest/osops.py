"""
A simple module for common OS Operations
"""

from pathlib import Path


def get_filename(path: str) -> str:
    """
    Get the filename from `path`
    """
    return Path(path).name


def get_foldername(path: str) -> str:
    """
    Get the last foldername from `path`
    """
    return Path(path).parent.name


def join(path: str, other: str) -> str:
    """
    Join `other` to path if path is a folder. Otherwise raise an error.
    """
    dir_path = Path(path)
    if dir_path.is_dir():
        return dir_path.joinpath(other).name
    raise AttributeError("`path` should be a folder.")
