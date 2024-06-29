import os

from app.constants import PathConstants


def read_static_file(file_path):
    path = os.path.join(PathConstants.STATIC_PATH, file_path)
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
