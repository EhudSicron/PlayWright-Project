from time import sleep
from HW1.classes.connection import Connection
from HW1.pages.Cart_page import Cart_page
from HW1.pages.checkout_page import Checkout_page
from HW1.pages.login_page import Login_page
from HW1.pages.product_page import Product_page
from HW1.pages.products_page import Products_page



#############   Main  ##############
#############   Main  ##############
con=Connection("chromium",100)
page = con.new_page()
print("Start test 3 - remove products")
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
cart_page.remove_prod_from_cart("Sauce Labs Backpack")
cart_page.remove_prod_from_cart("Sauce Labs Bike Light")
# checkout
cart_page.checkout_cart()
checkout_page = Checkout_page(page)

print("End test 3 - remove products")
sleep(3)
