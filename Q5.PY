<<<<<<< HEAD


class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


class Cow(Animal):
    def sound(self):
        print("Cow moos")


d = Dog("SHERU")
c = Cat("MITHI")
w = Cow("RANI")

d.sound()
c.sound()
w.sound()
=======
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)

b1 = Book(101, "Python Programming", "John Smith")
b2 = Book(102, "Data Science", "Alice Brown")
b3 = Book(103, "Machine Learning", "David Wilson")

b1.display()
print()

b2.display()
print()

b3.display()
>>>>>>> 311fd1035d158aae48cdc680a3b52c4edde99c26
