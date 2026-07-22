from playwright.sync_api import Page, expect
from tests.ui.pages.base_page import BasePage

class APIDocsPage(BasePage):
    """Page Object Model representing the SentinelDQ FastAPI Swagger UI."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.title_header = page.locator(".title")
        self.validation_endpoint = page.get_by_text("/api/v1/validation/run")
        self.accounts_endpoint = page.get_by_text("/api/v1/accounts")

    def navigate(self, base_url: str = "http://localhost:8000"):
        """Navigates to the Swagger documentation endpoint."""
        self.navigate_to(f"{base_url}/docs")

    def verify_header_title(self, expected_title: str = "SentinelDQ Platform API"):
        """Verifies the header text within the Swagger UI."""
        expect(self.title_header).to_contain_text(expected_title)

    def verify_validation_endpoint_visible(self):
        """Verifies that the validation run endpoint is visible."""
        expect(self.validation_endpoint).to_be_visible()
