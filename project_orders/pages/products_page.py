from project_orders.pages.basepage import BasePage


class Products_page(BasePage):
    def __init__(self,page):
        super().__init__(page)

    __PRODUCT_LIST=".inventory_item"
    __PRODUCT_NAME=".inventory_item_name"
    __PRODUCT_SELECT="[id^='add-to-cart']"
    __Cart = ".shopping_cart_link"
    __PRODUCT_PAGE = ""


    def add_to_cart(self, product_description):
        prodc_list=self.page.locator(self.__PRODUCT_LIST)
        count = prodc_list.count()
        print(count)
        for i in range(count):
            text = self.get_text(prodc_list.nth(i).locator(self.__PRODUCT_NAME))
            print(text)
            if text == product_description:
                print(f"Product name: {product_description}")
                self.click(prodc_list.nth(i).locator(self.__PRODUCT_SELECT))
                break
    def go_to_product(self, product_description):
        prodc_list=self.page.locator(self.__PRODUCT_LIST)
        count = prodc_list.count()
        print(count)
        for i in range(count):
            text = self.get_text(prodc_list.nth(i).locator(self.__PRODUCT_NAME))
            if text == product_description:
                print(f"Product name: {product_description}")
                self.click(prodc_list.nth(i).locator(self.__PRODUCT_NAME))
                break
    def goto_cart(self):
        self.page.locator(self.__Cart).click()



