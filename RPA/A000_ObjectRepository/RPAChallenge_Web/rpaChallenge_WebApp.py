from playwright.sync_api import Page, Locator

class RPAChallenge():
    def __init__(self, page: Page):
        self.page = page
    
    def get_locator(self, selector: str) -> Locator:
        """
        Returns a Playwright Locator object for the given selector.
        """
        return self.page.locator(selector)

    def set_text(self,selector: str, value: str):
        self.page.fill(selector, value)
    
    def click(self, selector: str):
        self.page.click(selector)
    