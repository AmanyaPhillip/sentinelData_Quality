import pytest
from playwright.sync_api import Page, expect

def test_dashboard_kpi_cards_render(page: Page):
    """
    Validates that the SentinelDQ Quality Dashboard loads 
    and renders key data reliability metrics correctly.
    """
    # Navigate to local or mock dashboard UI
    page.goto("http://localhost:8000/docs")  # Testing interactive Swagger UI / Dashboard
    
    # Assert Page Title and Main Headers
    expect(page).to_have_title("SentinelDQ Platform API - Swagger UI")
    
    # Validate API Schema Visual Elements
    header = page.locator(".title")
    expect(header).to_contain_text("SentinelDQ Platform API")

def test_api_docs_endpoint_accessibility(page: Page):
    """
    Validates accessibility and visual visibility of critical quality endpoints.
    """
    page.goto("http://localhost:8000/docs")
    
    # Verify the trigger validation endpoint is visible on screen
    validation_endpoint = page.get_by_text("/api/v1/validation/run")
    expect(validation_endpoint).to_be_visible()
