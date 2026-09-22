import os
from pathlib import path as p

def file_fs(file: str):
    """ Returns the total number of bytes """
    path = path(file)

    if not path.is_file():
        raise FileNotFoundError(f"File not found : {file}")

    retrun path.stat().st_size
