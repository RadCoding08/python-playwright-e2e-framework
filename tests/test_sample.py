# tests/test_sample.py
def test_google_title(browser_context):
    page = browser_context
    page.goto("https://www.google.com")
    assert "Google" in page.title()