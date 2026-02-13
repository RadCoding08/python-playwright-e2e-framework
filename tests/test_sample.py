import pytest
from playwright.sync_api import sync_playwright

def test_google_title():
    #start Playwright
    with sync_playwright() as p:
        # Launch brownser in headless mode
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Go to Google
        page.goto("https://www.google.com")
        
        # Assert title contains "Google"
        assert "Google" in page.title()
        
        # Close browser
        browser.close()