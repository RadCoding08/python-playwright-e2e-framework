# pages/youtube_page.py

class YouTubePage:
    def __init__(self, page):
        self.page = page
        self.search_box = "input#search"
        self.search_button = "button#search-icon-legacy"

    def go_to_homepage(self):
        """Open YouTube homepage"""
        self.page.goto("https://www.youtube.com")

    def search(self, text):
        """Type text in search box and click search button"""
        self.page.fill(self.search_box, text)
        self.page.click(self.search_button)

    def get_title(self):
        """Return the page title"""
        return self.page.title()