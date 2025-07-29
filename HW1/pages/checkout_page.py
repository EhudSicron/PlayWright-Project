from HW1.pages.basepage import BasePage


class Checkout_page(BasePage):
    def __init__(self,page):
        super().__init__(page)

    __FIRST_NAME_FIELD="#first-name"
    __LAST_NAME_FIELD = "#last-name"
    __ZIP_FIELD="#postal-code"
    __CONTINUE= "#continue"
    __CANCEL = "#cancel"
    __MENU = "#react-burger-menu-btn"
    __ALL_ITEMS = "#inventory_sidebar_link"
    __ABOUT = "#about_sidebar_link"
    __LOGOUT = "#logout_sidebar_link"
    __RESET_APP = "#reset_sidebar_link"


    def fill_user_add(self,first_name,last_name,zip_name):
        self.fill_text(self.__FIRST_NAME_FIELD,first_name)
        self.fill_text(self.__LAST_NAME_FIELD, last_name)
        self.fill_text(self.__ZIP_FIELD, zip_name)

    def continue_order(self,):
        self.click(self.__CONTINUE)
    def cancel_order(self):
        self.click(self.__CANCEL)
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
