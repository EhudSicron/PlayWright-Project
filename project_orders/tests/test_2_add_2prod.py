from time import sleep
from project_orders.classes.connection import Connection
from project_orders.pages.Cart_page import Cart_page
from project_orders.pages.checkout_overview_page import Checkout_overview_page
from project_orders.pages.checkout_page import Checkout_page
from project_orders.pages.login_page import Login_page
from project_orders.pages.product_page import Product_page
from project_orders.pages.products_page import Products_page

class Test_2_add_2prod:
    def test_2_add_2prod(self):
        #############   Main  ##############
        con=Connection("chromium",100)
        page = con.new_page()
        print("Start test 2 - add 2 products")
        # run login test
        login_page=Login_page(page)
        login_page.page.goto("http://www.saucedemo.com")
        login_page.login("standard_user","secret_sauce")
        # find Prod 1 and add to cart
        products_page=Products_page(page)
        products_page.go_to_product("Sauce Labs Bike Light")
        product_page = Product_page(page)
        product_page.add_to_cart()
        product_page.page.go_back()
        # find Prod 2 and add to cart
        product_page = Product_page(page)
        products_page.go_to_product("Sauce Labs Backpack")
        product_page.add_to_cart()
        product_page.page.go_back()
        # go to cart
        products_page.goto_cart()
        cart_page = Cart_page(page)
        # checkout
        cart_page.checkout_cart()
        checkout_page = Checkout_page(page)
        checkout_page.fill_user_add("Ehud","Sicron","123")
        checkout_page.continue_order()
        # Checkout overview
        checkout_overview_page = Checkout_overview_page(page)
        checkout_overview_page.open_menu()
        checkout_overview_page.menu_about()
        page.go_back()
        checkout_overview_page.finish_order()
        print("End test 2 - add 2 products")
        sleep(3)
