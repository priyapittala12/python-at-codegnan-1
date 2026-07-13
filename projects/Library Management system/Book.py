class Book:
    library_name = "ABC Library"

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def details(self):
        status = "Available" if self.available else "Issued"
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}"

