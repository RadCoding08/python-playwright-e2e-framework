from pages.bing_page import BingPage

def test_bing_title(browser_context):
    page = browser_context
    bing = BingPage(page)

    bing.go_to_homepage()
    assert "Bing" in bing.get_title()