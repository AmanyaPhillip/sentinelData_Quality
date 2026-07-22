from playwright.sync_api import Page, expect

class BasePage:
    """Base Page Object containing common interactions for all UI pages."""

    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        """Navigates to the specified URL."""
        self.page.goto(url)

    def verify_title(self, expected_title: str):
        """Verifies that the page title matches expected string."""
        expect(self.page).to_have_title(expected_title)
