import os


def check_dir():
    """
    Python program to check if a directory exists.
    """
    paths = ['./static', './tmp']
    for path in paths:
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
