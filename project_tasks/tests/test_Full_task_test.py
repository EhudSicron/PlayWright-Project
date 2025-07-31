from time import sleep

from project_tasks.classes.connection import Connection
from project_tasks.pages.tasks_page import Tasks_page

class Test_Full_task_test:
    def test_Full_task_test(self):
        #############   Main  ##############
        con=Connection("chromium",100)
        page = con.new_page()
        page.goto("http://www.mytinytodo.net/demo/")
        tasks_page=Tasks_page(page)
        tasks_page.goto_list("Todo")
        tasks_page.add_task_full("Full task",'2',
                                 "Note full task","Full task Tag",'15-5-2018')
        tasks_page.add_task_full("Full task 2",'1',
                                 "Note full task 2","Full task Tag 2",'1-4-2020')

        sleep(5)