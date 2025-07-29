from time import sleep

from HW1.classes.connection import Connection
from HW1.pages.login_page import Login_page
from HW1.pages.product_page import Product_page
from HW1.pages.products_page import Products_page
from playwright.sync_api import Page
from HW1.pages.basepage import BasePage
#############   Main  ##############
class Test1_login:
    def __init__(self, page:Page, login_page:Login_page=None, products_page:Products_page=None, product_page:Product_page=None):
        #self.connection=connection
        self.login_page = login_page
        self.page=page



    def run_test1_login(self):
        print("Start test 1 - login")
        # con=Connection("chromium",50,"http://www.saucedemo.com")
        self.login_page=Login_page(self.page)
        self.login_page.page.goto("http://www.saucedemo.com")
        self.login_page.login("standard_user","secret_sauce")
        print("End test 1 - login")
        sleep(3)