# tests/test_duckduckgo_pom.py

from pages.duckduckgo_page import DuckDuckGoPage

def test_duckduckgo_title(browser_context):
    page = browser_context
    duckduckgo = DuckDuckGoPage(page)

    duckduckgo.go_to_homepage()
    assert "DuckDuckGo" in duckduckgo.get_title()