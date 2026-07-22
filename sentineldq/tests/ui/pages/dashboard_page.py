from playwright.sync_api import Page, expect
from tests.ui.pages.base_page import BasePage

class DashboardPage(BasePage):
    """Page Object Model representing the SentinelDQ Quality Dashboard UI."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.kpi_cards = page.locator(".kpi-card")
        self.metrics_overview = page.locator("#metrics-overview")

    def navigate(self, base_url: str = "http://localhost:8000"):
        """Navigates to the quality dashboard root."""
        self.navigate_to(base_url)
