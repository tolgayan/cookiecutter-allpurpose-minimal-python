"""
Script to provide utility funcitons.
"""


import yaml


def get_config(path: str) -> dict:
    """Import yaml config file from a given path.

    Args:
        path (str): Path to the yaml file

    Returns:
        dict: yaml file as a dictionary
    """
    with open(path, "r") as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)