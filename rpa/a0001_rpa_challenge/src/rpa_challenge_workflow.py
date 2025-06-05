from pathlib import Path
import sys

#Add python-project path to module search list of paths to import project module
current_dir = Path(__file__).parent
project_root = current_dir.parent.parent.parent
if project_root not in  sys.path:
    sys.path.insert(0, str(project_root))

#Import project modules
from rpa.a000_object_repository.RPAChallenge_Web.Inputform_screen import InputForm

class RPAChallengeWorkflow:

    def __init__(self, page):
        self.page = page
        self.inputform = InputForm(self.page)

    def lauchApplication(self, url: str):
        try:
            self.page.goto(url, timeout=120000)
            self.page.wait_for_timeout(2000)
        except Exception as e:
            raise Exception(f"Error line no: {e.__traceback__.tb_lineno} & Error description: {str(e)}")

    def fill_and_submit_form(self, page, data):
        try:
            self.inputform.get_firstName_input().fill(data["firstName"])
            self.inputform.get_lastname_input().fill(data["lastName"])
            self.inputform.get_email_input().fill(data["emailID"])
            self.inputform.get_address_input().fill(data["address"])
            self.inputform.get_roleInCompany_input().fill(data["roleInCompany"])
            self.inputform.get_companyName_input().fill(data["companyName"])
            self.inputform.get_phoneNumber_input().fill(data["phoneNumber"])
            page.wait_for_timeout(2000)
            
            self.inputform.get_submit_button().click()
            page.wait_for_timeout(2000)
        except Exception as e:
            raise Exception(f"Error line no: {e.__traceback__.tb_lineno} & Error description: {str(e)}")


#TESTING PURPOSE ONLY
if __name__ == "__main__":
    rpa_challenge_url = "https://rpachallenge.com/"
    data = {"firstName": "Sunil",
            "lastName": "S",
            "emailID": "sunil@gmail.com",
            "address":"#1234",
            "roleInCompany": "engineer",
            "companyName": "Infosys",
            "phoneNumber": "1234567890"}

    inputData = [data for i in range(10)]

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        RPAChallengeWorkflow  = RPAChallengeWorkflow(page)
        RPAChallengeWorkflow.lauchApplication(rpa_challenge_url)

        for data in inputData:
            RPAChallengeWorkflow.fill_and_submit_form(page, data)

        pass
    

