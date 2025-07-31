from playwright.sync_api import sync_playwright


class Connection:
    def __init__(self,browser_name,speed):

        self.speed = speed
        self.__browser_name = browser_name
        # the page variable should be set last after link and speed
        #self.page1 = self.init_page()

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, value):
        self.__speed=value
    @property
    def browser_name(self):
        return self.__browser_name
    @browser_name.setter
    def browser_name(self, value):
        self.__browser_name=value


    def new_page(self):
        p = sync_playwright().start()
        match self.browser_name:
            case "chromium":
                current_browser1 =   p.chromium.launch(headless=False, slow_mo=self.speed, args=["--start-maximized"])
            case "firefox":
                current_browser1 = p.firefox.launch(headless=False, slow_mo=self.speed, args=["--start-maximized"])
            case _:
                current_browser1 = p.chromium.launch(headless=False, slow_mo=self.speed, args=["--start-maximized"])
        page = current_browser1.new_page()
        page.set_viewport_size({"width": 1360, "height": 768})  # Assuming a common screen resolution
        page.goto("https://www.google.com")
        return page




