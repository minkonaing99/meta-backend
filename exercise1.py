#Exercise: Define a Class

class House:
    num_rooms = 5
    bathrooms = 2
    
    def cost_evaluation(self) -> None:
        print(self.num_rooms + self.bathrooms)
        
house = House()
House.num_rooms  = 10
print(House.num_rooms)
print(house.num_rooms)

bravo = 3
b = B()
class B:
    bravo = 5
    print("Inside class B")
c = B()
print(b.bravo)