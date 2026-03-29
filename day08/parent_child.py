# Parent/super/base class
# Child/sub/derived class


class Employee:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last
        
class Supervisors(Employee):
    def __init__(self, name, last, password):
        super().__init__(name, last)
        self.password = password
        
class Chefs(Employee):
    def leave_request(self, days):
        return "May I take a leave for "+ str(days) + "days"
    
adrian = Supervisors("Adrian", "A", "apple")
emily = Chefs("emily", "E")
juno = Chefs("Juno", "J")


print(emily.leave_request(3))
print(adrian.password)
print(juno.last)

print(issubclass( Chefs,  Employee))
print(issubclass( Employee,  Chefs))

print(isinstance(juno, Employee))


class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()