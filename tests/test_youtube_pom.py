# tests/test_youtube_pom.py

from pages.youtube_page import YouTubePage

def test_youtube_title(browser_context):
    page = browser_context
    youtube = YouTubePage(page)

    youtube.go_to_homepage()
    assert "YouTube" in youtube.get_title()