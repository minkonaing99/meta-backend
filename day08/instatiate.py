class Recipe():
    def __init__(self , dish, item, time)-> None:
        self.dish = dish
        self.item = item
        self.time = time
        
        
    def contents(self):
        print(f"The {self.dish} has {str(self.item)} and takes {str(self.time)} min to prepare")
        
        
        
pizza = Recipe("Pizza" , ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta" , ["penne", "sauce"], 55)


pizza.contents()
pasta.contents()