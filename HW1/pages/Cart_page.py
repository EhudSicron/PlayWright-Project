from HW1.pages.basepage import BasePage

class Cart_page(BasePage):
    def __init__(self,page):
        super().__init__(page)

    __ADD_TO_Cart = "#add-to-cart"
    __GO_TO_CART = "#shopping_cart_container"
    __PRODUCTS_LIST = ".cart_item"
    __PRODUCT_NAME = ".inventory_item_name"
    __PRODUCT_REMOVE= "[id^='remove-']"
    __CHECK_OUT = "#checkout"
    __CONTINUE_SHOP_BUT = "#continue-shopping"

    def remove_prod_from_cart(self, product_description):
        prodc_list=self.page.locator(self.__PRODUCTS_LIST)
        count = prodc_list.count()
        print(count)
        self.page
        for i in range(count):
            text = self.get_text(prodc_list.nth(i).locator(self.__PRODUCT_NAME))
            print(text)
            if text == product_description:
                print(f"Product name: {product_description}")
                prodc_list.nth(i).locator(self.__PRODUCT_REMOVE).click()
                break
    def checkout_cart(self):
        self.page.locator(self.__CHECK_OUT).click()
    def continue_shopping(self):
        self.page.locator(self.__CONTINUE_SHOP_BUT).click()