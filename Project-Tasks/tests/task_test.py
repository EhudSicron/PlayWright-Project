from time import sleep
from HW2.classes.connection import Connection
from HW2.pages.tasks_page import Tasks_page


#############   Main  ##############
con = Connection("chromium", 100)
page = con.new_page()
page.goto("http://www.mytinytodo.net/demo/")
tasks_page=Tasks_page(page)
tasks_page.goto_list("Todo")
tasks_page.add_simple_task("First Task1")
sleep(5)

