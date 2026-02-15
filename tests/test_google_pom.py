from pages.google_page import GooglePage


def test_google_title(browser_context):
    page = browser_context

    google = GooglePage(page)
    google.go_to_homepage()

    assert "Google" in google.get_title()