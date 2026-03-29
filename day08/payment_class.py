class Payment():
    def __init__(self, price):
        self.__final_price = price + price*0.05
        
    def get_final_price(self):
        return self.__final_price
    
    def set_final_price(self, discount):
        self.__final_price = self.__final_price - self.__discount_calculated(discount)
    def __discount_calculated(self, discount):
        return self.__final_price*(discount/100)
        

bakery = Payment(100)

print(bakery.get_final_price())
bakery.set_final_price(90)
print(bakery.get_final_price())
