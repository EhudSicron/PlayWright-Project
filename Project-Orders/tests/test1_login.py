from time import sleep

from HW1.classes.connection import Connection
from HW1.pages.login_page import Login_page

#############   Main  ##############
con=Connection("chromium",100)
page = con.new_page()

print("Start test 1 - login")
# con=Connection("chromium",50,"http://www.saucedemo.com")
login_page=Login_page(page)
login_page.page.goto("http://www.saucedemo.com")
login_page.login("standard_user","secret_sauce")
print("End test 1 - login")
sleep(3)