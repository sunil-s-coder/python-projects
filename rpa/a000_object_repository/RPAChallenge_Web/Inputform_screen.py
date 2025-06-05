from playwright.sync_api import sync_playwright
import sys
from pathlib import Path

#Add python-project path to module search list of paths to import project module
current_dir = Path(__file__).parent
project_root = current_dir.parent.parent.parent
if project_root not in  sys.path:
    sys.path.insert(0, str(project_root))

from rpa.a000_object_repository.RPAChallenge_Web.rpa_challenge_app import RPAChallengeApp

class InputForm(RPAChallengeApp):
    #Define selectors as constants
    FIRSTNAME_INPUT = "rpa_challenge_app.input_form.FIRSTNAME_INPUT"
    LASTNAME_INPUT = "rpa_challenge_app.input_form.LASTNAME_INPUT"
    PHONENUMBER_INPUT = "rpa_challenge_app.input_form.PHONENUMBER_INPUT"
    EMAIL_INPUT = "rpa_challenge_app.input_form.EMAIL_INPUT"
    ADDRESS_INPUT = "rpa_challenge_app.input_form.ADDRESS_INPUT"
    ROLEINCOMPANY_INPUT = "rpa_challenge_app.input_form.ROLEINCOMPANY_INPUT"
    COMPANYNAME_INPUT = "rpa_challenge_app.input_form.COMPANYNAME_INPUT"
    SUBMIT_BUTTON = "rpa_challenge_app.input_form.SUBMIT_BUTTON"

    def __init__(self, page):
        super().__init__(page)

    def get_firstName_input(self):
        return self.get_locator(self.FIRSTNAME_INPUT)
    
    def get_lastname_input(self):
        return self.get_locator(self.LASTNAME_INPUT)

    def get_phoneNumber_input(self):
        return self.get_locator(self.PHONENUMBER_INPUT)

    def get_email_input(self):
        return self.get_locator(self.EMAIL_INPUT)

    def get_address_input(self):
        return self.get_locator(self.ADDRESS_INPUT)
    
    def get_roleInCompany_input(self):
        return self.get_locator(self.ROLEINCOMPANY_INPUT)
    
    def get_companyName_input(self):
        return self.get_locator(self.COMPANYNAME_INPUT)

    def get_submit_button(self):
        return self.get_locator(self.SUBMIT_BUTTON)