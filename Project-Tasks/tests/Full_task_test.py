from time import sleep

from playwright.sync_api import Page
from HW1.pages.basepage import BasePage
from HW2.classes.connection import Connection
from HW2.pages.tasks_page import Tasks_page


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