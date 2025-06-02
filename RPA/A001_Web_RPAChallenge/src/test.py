from playwright.sync_api import sync_playwright

# RPA/A001_Web_RPAChallenge/src/test.py
import sys
import os

# Get the absolute path of the directory containing the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up three levels to reach 'python-projects/'
# current_dir: .../RPA/A001_Web_RPAChallenge/src
# 1sirname: .../RPA/A001_Web_RPAChallenge
# 2nd os.path.dit os.path.drname: .../RPA
# 3rd os.path.dirname: .../python-projects
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))

# Add the project root to sys.path
sys.path.insert(0, project_root) # Insert at the beginning to give it priority

# Now your imports should work
from RPA.A000_ObjectRepository.RPAChallenge_Web.Inputform_screen import InputForm
# ... rest of your test.py code

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rpachallenge.com/")
    page.wait_for_timeout(2000)

    inputform = InputForm(page)
    page.wait_for_timeout(2000)

    inputform.get_firstName_input().fill("Sunil")
    inputform.get_lastname_input().fill("s")
    inputform.get_email_input().fill("sunil@gmail.com")
    inputform.get_address_input().fill("#1234")
    inputform.get_roleInCompany_input().fill("engineer")
    inputform.get_companyName_input().fill("Infosys")
    inputform.get_phoneNumber_input().fill("133456790")
    inputform.get_submit_button().click()
    
    page.wait_for_timeout(2000)
