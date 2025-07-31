from time import sleep

from project_tasks.classes.connection import Connection
from project_tasks.pages.tasks_page import Tasks_page

class Test_task_test:
    def test_task_test(self):
        #############   Main  ##############
        con = Connection("chromium", 100)
        page = con.new_page()
        page.goto("http://www.mytinytodo.net/demo/")
        tasks_page=Tasks_page(page)
        tasks_page.goto_list("Todo")
        tasks_page.add_simple_task("First Task1")
        sleep(5)

