from project_tasks.pages.basepage import BasePage


class Tasks_page(BasePage):
    def __init__(self,page):
        super().__init__(page)

    __LIST_TODO_TAB="#list_2"
    __LIST_TABS = ".mtt-tabs.ui-sortable>[id^='list']"
    __TASK_FIELD = "#task"
    __TASK_BTN = "#newtask_submit"
    __Task_All_FIELDS_BNT = "#newtask_adv"
    __NEW_TASK_DISC_FIELD =".form-row>[name='task']"
    __NEW_TASK_NOTE_FIELD = ".form-row>[name='note']"
    __NEW_TASK_TAG_FIELD = "#edittags"
    __NEW_TASK_PRIORITY_LIST = "#taskedit_form > div > div:nth-child(1) > select"
    __NEW_TASK_DATE_BTN = ".ui-datepicker-trigger"
    __NEW_TASK_YEARS_LIST = ".ui-datepicker-year"
    __NEW_TASK_MONTH_LIST = ".ui-datepicker-month"
    __NEW_TASK_DAY_LIST = "[data-handler='selectDay']"
    __NEW_TASK_SAVE = ".form-row.form-bottom-buttons >[type='submit']"
    __SEARCH = "#search"
    __TASKS_LIST = "#tasklist [id^='taskrow']"
    __NEW_LIST_TAB_BTN = ".mtt-tabs-new-button"
    __NEW_LIST_NAME = "#modalTextInput"
    __NEW_LIST_OK = "#btnModalOk"
    def goto_list(self,tasks_tab):
        list_tab=self.page.locator(self.__LIST_TABS)
        count = list_tab.count()
        for i in range(count):
            text = self.get_text(list_tab.nth(i))
            print(f"text new list = {text}")
            if  text == tasks_tab:
                self.click(list_tab.nth(i))
                break

    def add_simple_task (self, task_description):
        self.fill_text(self.__TASK_FIELD,task_description)
        self.hover(self.__TASK_BTN)
        self.click(self.__TASK_BTN)
    def add_task_full(self,task_description,priority,note,tag,date):
        self.hover(self.__Task_All_FIELDS_BNT)
        self.click(self.__Task_All_FIELDS_BNT)
        self.fill_text(self.__NEW_TASK_DISC_FIELD, task_description)
        self.fill_text(self.__NEW_TASK_NOTE_FIELD, note)
        self.fill_text(self.__NEW_TASK_TAG_FIELD, tag)
        self.mark_priority(priority)
        self.fill_date(date)
        self.click(self.__NEW_TASK_SAVE)


    def mark_priority(self,priority):
        priority_list= self.page.locator(self.__NEW_TASK_PRIORITY_LIST)
        priority_list.select_option(value=priority)

    def fill_date(self,date):
        # date e.g. = 23-2-2018
        year=date.split("-")[2]
        month=date.split("-")[1]
        day= date.split("-")[0]
        print(f"day{day} , month {month}, day {year}")
        self.hover(self.__NEW_TASK_DATE_BTN)
        self.click(self.__NEW_TASK_DATE_BTN)
        #self.page.click(self.__NEW_TASK_YEARS_LIST)
        year_list = self.page.locator(self.__NEW_TASK_YEARS_LIST)
        year_list.select_option(value=year)
        month_list = self.page.locator(self.__NEW_TASK_MONTH_LIST)
        month_list.select_option(value=month)
        self.click(f"[data-date='{day}']")

    def find_tasks(self,search):
        self.fill_text(self.__SEARCH,search)
        num_tasks = self.page.locator(self.__TASKS_LIST).count()
        print(f"The number of tasks in the search results: {num_tasks}")
        return num_tasks

    def new_list(self,list_name):
        # self.page.once("dialog", lambda dialog: dialog.accept("list_name") or )
        self.click(self.__NEW_LIST_TAB_BTN)
        self.fill_text(self.__NEW_LIST_NAME,list_name)
        self.click(self.__NEW_LIST_OK)








