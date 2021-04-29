"""
A simple module for common OS Operations
"""

from os.path import basename, dirname


def get_filename(path: str) -> str:
    """
    Get the filename from `path`
    """
    return basename(path)


def get_foldername(path: str) -> str:
    """
    Get the last foldername from `path`
    """
    return basename(dirname(path))
