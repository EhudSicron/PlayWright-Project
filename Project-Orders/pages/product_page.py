from HW1.pages.basepage import BasePage


class Product_page(BasePage):
    def __init__(self,page):
        super().__init__(page)


    __ADD_TO_Cart = "#add-to-cart"
    __GO_TO_CART = "#shopping_cart_container"

    def add_to_cart(self):
        self.click(self.__ADD_TO_Cart)
    def go_to_cart(self):
        self.click(self.__GO_TO_CART)



