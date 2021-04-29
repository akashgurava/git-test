"""
A simple module for common OS Operations
"""

from os.path import basename


def get_filename(path: str) -> str:
    """
    Get the filename from `path`
    """
    return basename(path)
