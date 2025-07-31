from HW1.pages.basepage import BasePage


class Login_page(BasePage):
    def __init__(self,page):
        super().__init__(page)




    __USER_NAME_FIELD="#user-name"
    __PASSWORD_FIELD = "#password"
    __LOGIN_FIELD="#login-button"


    def login(self,first_name,last_name):
        self.fill_text(self.__USER_NAME_FIELD,first_name)
        self.fill_text(self.__PASSWORD_FIELD, last_name)
        self.click(self.__LOGIN_FIELD)


