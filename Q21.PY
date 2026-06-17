class Library:
    def __init__(self, book):
        self.book = book

    def display(self):
        print("Book:", self.book)

l = Library("Python Programming")
l.display()