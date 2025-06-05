import os
import sys
from pathlib import Path
from playwright.sync_api import Page, Locator

#Add python-project path to module search list of paths to import project module
current_dir = Path(__file__).parent
project_root = current_dir.parent.parent.parent
if project_root not in  sys.path:
     sys.path.insert(0, str(project_root))

from rpa.a000_utils.read_config import config_reader

class RPAChallengeApp():
    def __init__(self, page: Page):
        self.page = page
        self.locators = self._load_locators()
    
    def _load_locators(self):
        """
        Initialized the path of the locator.yaml file
        Call read config to read yaml file and returns dictionary
        """
        locators_config_file = Path(__file__).parent / "locators.yaml"
        return config_reader(locators_config_file)

    def get_locator(self, selector: str) -> Locator:
        """
        Returns a Playwright Locator object for the given selector.
        """
        keys = selector.split(".")
        locator_dict = self.locators

        for key in keys:
            if key in locator_dict.keys():
                locator_dict = locator_dict[key]
            else:
                KeyError(f"Selector path {selector} not found in Config. Missing key {key} in config dicionary {locator_dict}")
                 
        return self.page.locator(locator_dict)
