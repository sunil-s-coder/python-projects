from playwright.sync_api import Page

class RPAChallenge:
    def __init__(self, page: Page):
        self.page = page
    
    def set_text(self,selector: str, value: str):
        self.page.fill(selector, value)
    
    def click(self, selector: str):
        self.page.click(selector)
    