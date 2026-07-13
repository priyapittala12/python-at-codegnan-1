class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return "Book Added Successfully"

    def display_books(self):
        if len(self.books) == 0:
            return "No Books Available"

        for book in self.books:
            print(book.details())

    def issue_book(self, book_id):
        book_id = int(book_id)    
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    return "Book Issued Successfully"
                else:
                    return "Book Already Issued"
        return "Book Not Found"
    
    def return_book(self, book_id):
        book_id = int(book_id)
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    return "Book Returned Successfully"
                else:
                    return "Book Already Available"
        return "Book Not Found"
