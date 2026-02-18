class MyFirstClass():
    print("Who wrote this?")
    index = "Author-book"
    
    def __init__(self, philosopher, book) -> None:
        self.philosopher = philosopher
        self.book = book
    
    def hand_list(self):
        print(self.index)
        print(self.philosopher + "wrote the book: " + self.book)
        
whodunnit = MyFirstClass("Sun Tzu" , "The Art")

whodunnit.hand_list()


# without storing parameter in object
class MyFirstClass:
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)


whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")
