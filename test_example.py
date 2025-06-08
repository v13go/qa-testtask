import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    title_regex = re.compile(r"Fast and reliable end-to-end testing for modern web apps \| Playwright")
    expect(page).to_have_title(title_regex)

