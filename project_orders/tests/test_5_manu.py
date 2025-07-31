from time import sleep

from project_orders.classes.connection import Connection
from project_orders.pages.Cart_page import Cart_page
from project_orders.pages.checkout_page import Checkout_page
from project_orders.pages.login_page import Login_page
from project_orders.pages.products_page import Products_page

class Test_5_manu:
    def test_5_manu(self):
        #############   Main  ##############
        con=Connection("chromium",100)
        page = con.new_page()
        print("Start test 5 - Manu")
        # run login test
        login_page=Login_page(page)
        login_page.page.goto("http://www.saucedemo.com")
        login_page.login("standard_user","secret_sauce")
        # find Prod 1 and add to cart
        products_page=Products_page(page)
        # go to cart
        products_page.goto_cart()
        cart_page = Cart_page(page)
        # checkout
        cart_page.checkout_cart()
        checkout_page = Checkout_page(page)
        # Checkout menu about
        checkout_page.open_menu()
        checkout_page.menu_about()
        page.go_back()

        # Checkout menu all items
        checkout_page.open_menu()
        checkout_page.menu_all_items()

        # Go to cart checkout
        products_page.goto_cart()
        cart_page.checkout_cart()

        # Checkout menu logout
        checkout_page.open_menu()
        checkout_page.menu_logout()

        print("End test 5 - Manu")
        sleep(3)
