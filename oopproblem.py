class ShoppingCart(object):
    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        if isinstance(quantity, int) and isinstance(price, int):
            self.total += (quantity * price)
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity, price):
        if isinstance(quantity, int) and isinstance(price, int):
    	    if item_name in self.items and (quantity * price) < self.total: #check this
                if quantity >= self.items[item_name]:
                    self.total -= (self.items[item_name] * price)
                    del(self.items[item_name])
                else:
                    self.total -= (quantity * price)
                    self.items[item_name] -= quantity

    def checkout(self, cash_paid):
        if cash_paid < self.total:
            return 'Cash paid not enough'
        else:
            return cash_paid - self.total

class Shop(ShoppingCart):
    def __init__(self):
        self.quantity = 100

    def remove_item(self):
        self.quantity -= 1

shopcart = ShoppingCart()
shopcart.add_item(True , 2, 1000)
shopcart.add_item('pens', 13, 500)

shopcart.remove_item('pens', 11, '1000')
print(shopcart.items)
print(shopcart.total)