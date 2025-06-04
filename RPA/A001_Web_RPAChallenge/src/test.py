from playwright.sync_api import sync_playwright
import sys
from pathlib import Path

#Add python-project path to module search list of paths to import project module
current_dir = Path(__file__).parent
project_root = current_dir.parent.parent.parent
if project_root not in  sys.path:
    sys.path.insert(0, str(project_root))

#Import project modules
from RPA.A000_ObjectRepository.RPAChallenge_Web.Inputform_screen import InputForm

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rpachallenge.com/", timeout=120000)
    page.wait_for_timeout(2000)

    inputform = InputForm(page)
    page.wait_for_timeout(2000)

    for i in range(5):
        inputform.get_firstName_input().fill("Sunil")
        inputform.get_lastname_input().fill("s")
        inputform.get_email_input().fill("sunil@gmail.com")
        inputform.get_address_input().fill("#1234")
        inputform.get_roleInCompany_input().fill("engineer")
        inputform.get_companyName_input().fill("Infosys")
        inputform.get_phoneNumber_input().fill("133456790")
        page.wait_for_timeout(2000)
        
        inputform.get_submit_button().click()
        page.wait_for_timeout(2000)

    pass