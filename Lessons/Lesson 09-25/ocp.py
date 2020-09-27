class Discount:

    def __init__(self, customer):
        self.customer = customer

    # def get_discounted_price(self, price):
    #     if self.customer.type == 'vip':
    #         return price * 0.85
    #     if self.customer.type == 'svip':
    #         return price * 0.8
        
    #     return price * 0.9

    def get_discounted_price(self, price):
        return price*0.9

class VIPDiscount(Discount):

    def get_discounted_price(self, price):
        return price * 0.8
