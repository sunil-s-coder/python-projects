# This file is part of the Python-projects repository.
# Licensed under the MIT License – see LICENSE file for details.

import yaml

def config_reader(config_file_path):
    """
    Reads and parses a YAML configuration file.

    Args:
        config_file_path (str): Path to the YAML config file.

    Returns:
        dict: Parsed configuration data.

    Raises:
        Exception: If file reading or parsing fails, includes error line number and description.
    """
    try:
        with open(config_file_path,'r') as f:
            config = yaml.safe_load(f)
            return config
    except Exception as e:
        raise Exception(f"Line no: {e.__traceback__.tb_lineno} | Description: {str(e)}")
