from HW1.pages.basepage import BasePage


class Checkout_overview_page(BasePage):
    def __init__(self,page):
        super().__init__(page)


    __FINISH = "#finish"
    __MENU = "#react-burger-menu-btn"
    __ALL_ITEMS = "#inventory_sidebar_link"
    __ABOUT = "#about_sidebar_link"
    __LOGOUT = "#logout_sidebar_link"
    __RESET_APP = "#reset_sidebar_link"


    def finish_order(self,):
        self.click(self.__FINISH)
    def open_menu(self):
        self.hover(self.__MENU)
        self.click(self.__MENU)

    def menu_all_items(self):
        self.click(self.__ALL_ITEMS)

    def menu_about(self):
        self.click(self.__ABOUT)

    def menu_logout(self):
        self.click(self.__LOGOUT)

    def menu_reset_app(self):
        self.click(self.__RESET_APP)