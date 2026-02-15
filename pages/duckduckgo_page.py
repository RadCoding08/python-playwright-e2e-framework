# pages/duckduckgo_page.py

class DuckDuckGoPage:
    def __init__(self, page):
        self.page = page
        self.search_box = "input[name='q']"
        self.search_button = "input[id='search_button_homepage']"

    def go_to_homepage(self):
        """Open DuckDuckGo homepage"""
        self.page.goto("https://duckduckgo.com")

    def search(self, text):
        """Type text in search box and press Enter"""
        self.page.fill(self.search_box, text)
        self.page.press(self.search_box, "Enter")

    def get_title(self):
        """Return the page title"""
        return self.page.title()