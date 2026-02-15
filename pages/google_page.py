class GooglePage:
    def __init__(self, page):
        self.page = page
        self.search_box = "input[name='q']"

    def go_to_homepage(self):
        """Open the Google homepage."""
        self.page.goto("https://www.google.com")

    def get_title(self):
        """Return the page title."""
        return self.page.title()