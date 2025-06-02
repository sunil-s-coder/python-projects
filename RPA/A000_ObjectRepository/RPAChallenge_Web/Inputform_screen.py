from playwright.sync_api import sync_playwright

# RPA/A001_Web_RPAChallenge/src/test.py
import sys
import os

# Get the absolute path of the directory containing the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up three levels to reach 'python-projects/'
# current_dir: .../RPA/A001_Web_RPAChallenge/src
# 1st os.path.dirname: .../RPA/A001_Web_RPAChallenge
# 2nd os.path.dirname: .../RPA
# 3rd os.path.dirname: .../python-projects
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))

# Add the project root to sys.path
sys.path.insert(0, project_root) # Insert at the beginning to give it priority

# Now your imports should work
from RPA.A000_ObjectRepository.RPAChallenge_Web.rpaChallenge_WebApp import RPAChallenge
# ... rest of your test.py code

class InputForm(RPAChallenge):
    #Define selectors as constants
    FIRSTNAME_INPUT = "//*[text()='First Name']/following::input[1]"
    LASTNAME_INPUT = "//*[text()='Last Name']/following::input[1]"
    PHONENUMBER_INPUT = "//*[text()='Phone Number']/following::input[1]"
    EMAIL_INPUT = "//*[text()='Email']/following::input[1]"
    ADDRESS_INPUT = "//*[text()='Address']/following::input[1]"
    ROLEINCOMPANY_INPUT = "//*[text()='Role in Company']/following::input[1]"
    COMPANYNAME_INPUT = "//*[text()='Company Name']/following::input[1]"

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
        return self.get_locator(self.COMPANYNAME_INPUT)