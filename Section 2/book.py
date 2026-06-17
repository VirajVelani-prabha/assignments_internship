

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

book1 = Book("Python Programming", "John Smith", 450)
book2 = Book("Data Science Basics", "Alice Brown", 550)
book3 = Book("Machine Learning", "David Wilson", 650)

print("Book 1")
print("Title:", book1.title)
print("Author:", book1.author)
print("Price:", book1.price)

print("\nBook 2")
print("Title:", book2.title)
print("Author:", book2.author)
print("Price:", book2.price)

print("\nBook 3")
print("Title:", book3.title)
print("Author:", book3.author)
print("Price:", book3.price)