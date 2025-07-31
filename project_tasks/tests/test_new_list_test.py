from time import sleep

from project_tasks.classes.connection import Connection
from project_tasks.pages.tasks_page import Tasks_page

class Test_new_list_test:
    def test_new_list_test(self):
        #############   Main  ##############
        con = Connection("chromium", 100)
        page = con.new_page()
        page.goto("http://www.mytinytodo.net/demo/")
        tasks_page=Tasks_page(page)
        # Create a new tasks list TAB
        tasks_page.new_list("POM6")
        new_tasks_num = 2
        sleep(1)
        tasks_page.goto_list("POM6")
        # find and count all tasks in the new TAB
        old_num_tasks = tasks_page.find_tasks("")
        print(f"old_num_tasks: {old_num_tasks}")
        # Create 2 task in the new list TAB
        for i in range(new_tasks_num):
            tasks_page.add_simple_task(f"POM Task {i}")
            print(f"POM2 Task {i}")
            sleep(1)

        sleep(1)
        # find and count all tasks in the new TAB
        num_tasks =tasks_page.find_tasks("")
        print(f"num_tasks: {num_tasks}")
        actual_tasks_added =  num_tasks-old_num_tasks
        if  actual_tasks_added == new_tasks_num:
            print(f"PASS - All new tasks are in the list. num of tasks: {actual_tasks_added}")
        else:
            print(f"FAIL - Some of the tasks are missing. Actual: {actual_tasks_added} ")
        sleep(5)