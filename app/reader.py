import json
import yaml
from functools import partial


class UnsupportedFileTypeException(Exception):
    pass


def read_request_file(filepath) -> dict:
    """
    Reads a request file and returns its contents as a dictionary.
    The function supports YAML (.yml, .yaml) and JSON (.json) file formats.
    If the file format is not supported, an UnsupportedFileTypeException is raised.
    Args:
        filepath (str): The path to the request file.
    Returns:
        dict: The contents of the request file.
    Raises:
        UnsupportedFileTypeException: If the file format is not supported.
    """
    if filepath.endswith(".yml") or filepath.endswith(".yaml"):
        loader = partial(yaml.load, Loader=yaml.FullLoader)
    elif filepath.endswith(".json"):
        loader = json.load
    else:
        raise UnsupportedFileTypeException(filepath)

    with open(filepath, "r") as f:
        file_data = loader(f)

    return file_data
