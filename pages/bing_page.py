class BingPage:
    def __init__(self, page):
        self.page = page
        self.search_box = "input[name='q']"
        self.search_button = "input[id='sb_form_go']"

    def go_to_homepage(self):
        """Open Bing homepage"""
        self.page.goto("https://www.bing.com")

    def search(self, text):
        """Type text in search box and press Enter"""
        self.page.fill(self.search_box, text)
        self.page.press(self.search_box, "Enter")

    def get_title(self):
        """Return the page title"""
        return self.page.title()