import pytest
from playwright.sync_api import Page
from tests.ui.pages.api_docs_page import APIDocsPage

def test_api_docs_renders_correctly(page: Page):
    """
    Validates that the SentinelDQ Swagger API interface 
    renders key endpoints using Page Object Model.
    """
    api_docs = APIDocsPage(page)
    
    # Execution using POM methods
    api_docs.navigate()
    api_docs.verify_header_title("SentinelDQ Platform API")
    api_docs.verify_validation_endpoint_visible()

def test_dashboard_kpi_cards_render(page: Page):
    """
    Validates that the SentinelDQ Quality Dashboard / API docs load correctly using POM.
    """
    api_docs = APIDocsPage(page)
    api_docs.navigate()
    api_docs.verify_title("SentinelDQ Platform API - Swagger UI")
    api_docs.verify_header_title("SentinelDQ Platform API")
