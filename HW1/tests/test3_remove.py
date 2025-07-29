from time import sleep
from HW1.classes.connection import Connection
from HW1.pages.Cart_page import Cart_page
from HW1.pages.checkout_overview_page import Checkout_overview_page
from HW1.pages.checkout_page import Checkout_page
from HW1.pages.login_page import Login_page
from HW1.pages.product_page import Product_page
from HW1.pages.products_page import Products_page
from playwright.sync_api import Page
from HW1.tests.test1_login import Test1_login


#############   Main  ##############
class Test3_remove:
    def __init__(self, page:Page, connection:Connection=None, test1_login:Test1_login=None,
                 products_page:Products_page=None, product_page:Product_page=None, cart_page:Cart_page=None,
                 checkout_page:Checkout_page=None, checkout_overview_page:Checkout_overview_page=None):
        self.checkout_overview_page = checkout_overview_page
        self.checkout_page = checkout_page
        self.cart_page = cart_page
        self.connection=connection
        self.page=page
        self.test1_login = test1_login
        self.products_page = products_page
        self.product_page = product_page



    def run_test3_remove(self):
        print("Start test 3 - remove products")
        # run login test
        self.test1_login=Test1_login(self.page)
        self.test1_login.run_test1_login()
        # find Prod 1 and add to cart
        self.products_page=Products_page(self.page)
        self.products_page.go_to_product("Sauce Labs Bike Light")
        self.product_page = Product_page(self.page)
        self.product_page.add_to_cart()
        self.product_page.page.go_back()
        # find Prod 2 and add to cart
        self.product_page = Product_page(self.page)
        self.products_page.go_to_product("Sauce Labs Backpack")
        self.product_page.add_to_cart()
        self.product_page.page.go_back()
        # go to cart
        self.products_page.goto_cart()
        self.cart_page = Cart_page(self.page)
        self.cart_page.remove_prod_from_cart("Sauce Labs Backpack")
        self.cart_page.remove_prod_from_cart("Sauce Labs Bike Light")
        # checkout
        self.cart_page.checkout_cart()
        self.checkout_page = Checkout_page(self.page)

        print("End test 3 - remove products")
        sleep(3)
