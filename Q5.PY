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