from time import sleep

from project_orders.classes.connection import Connection
from project_orders.pages.login_page import Login_page


class Test_01_login:
#############   Main  ##############
    def test_01(self):
        con=Connection("chromium",100)
        page = con.new_page()

        print("Start test 1 - login")
        # con=Connection("chromium",50,"http://www.saucedemo.com")
        login_page=Login_page(page)
        login_page.page.goto("http://www.saucedemo.com")
        login_page.login("standard_user","secret_sauce")
        print("End test 1 - login")
        sleep(3)