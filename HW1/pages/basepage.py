from time import sleep

from playwright.sync_api import Page,Locator


class BasePage:
    """ Wrapper for Playwright operations """

    def __init__(self, page: Page):
        self.page = page


    def click(self, locator_or_selector) -> None:
        sleep(1)
        if isinstance(locator_or_selector, Locator):
            locator_or_selector.click()
        else:
            self.page.locator(locator_or_selector).click()
        print(self.page.url)

    def hover(self, locator) -> None:
        sleep(1)
        self.page.locator(locator).hover()

    def fill_text(self, locator, txt: str) -> None:
        self.page.locator(locator).fill(txt)

    def get_text(self, locator_or_selector) -> str:
        if isinstance(locator_or_selector, Locator):
            text = locator_or_selector.inner_text()
        else:
            text = self.page.locator(locator_or_selector).inner_text()
        return text
