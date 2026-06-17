class Book:
    library_name = "City Library"

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def display_book_info(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Library Name:", Book.library_name)

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name

b1 = Book(101, "Python Programming", "John Smith")
b2 = Book(102, "Data Science", "Alice Brown")

print("Before Changing Library Name:")
b1.display_book_info()
print()
b2.display_book_info()

Book.change_library_name("Central Library")

print("\nAfter Changing Library Name:")
b1.display_book_info()
print()
b2.display_book_info()