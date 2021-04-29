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
