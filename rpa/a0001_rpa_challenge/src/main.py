from playwright.sync_api import sync_playwright
from pathlib import Path
import sys

#Add python-project path to module search list of paths to import project module
current_dir = Path(__file__).parent
project_root = current_dir.parent.parent.parent
if project_root not in  sys.path:
    sys.path.insert(0, str(project_root))

#Import project modules
from rpa.a0001_rpa_challenge.src.rpa_challenge_workflow import RPAChallengeWorkflow

#RPA Challenge workflow
rpa_challenge_url = "https://rpachallenge.com/"
data = {"firstName": "Sunil",
        "lastName": "S",
        "emailID": "sunil@gmail.com",
        "address":"#1234",
        "roleInCompany": "engineer",
        "companyName": "Infosys",
        "phoneNumber": "1234567890"}

inputData = [data for i in range(10)]


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    RPAChallengeWorkflow  = RPAChallengeWorkflow(page)
    RPAChallengeWorkflow.lauchApplication(rpa_challenge_url)

    for data in inputData:
        RPAChallengeWorkflow.fill_and_submit_form(page, data)

    page.close()