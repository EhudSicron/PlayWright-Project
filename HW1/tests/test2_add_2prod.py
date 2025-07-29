from time import sleep
from HW1.classes.connection import Connection
from HW1.pages.Cart_page import Cart_page
from HW1.pages.checkout_overview_page import Checkout_overview_page
from HW1.pages.checkout_page import Checkout_page
from HW1.tests.test1_login import Test1_login
from HW1.pages.product_page import Product_page
from HW1.pages.products_page import Products_page
from playwright.sync_api import Page



#############   Main  ##############
class Test2_add_2prod:
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



    def run_test2_ad_2prod(self):
        print("Start test 2 - add 2 products")
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
        # checkout
        self.cart_page.checkout_cart()
        self.checkout_page = Checkout_page(self.page)
        self.checkout_page.fill_user_add("Ehud","Sicron","123")
        self.checkout_page.continue_order()
        # Checkout overview
        self.checkout_overview_page = Checkout_overview_page(self.page)
        self.checkout_overview_page.open_menu()
        self.checkout_overview_page.menu_about()
        self.page.go_back()
        self.checkout_overview_page.finish_order()
        print("End test 2 - add 2 products")
        sleep(3)
