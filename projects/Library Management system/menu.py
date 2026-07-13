from Book import Book
from Library import Library

class Menu:
    def __init__(self):
        self.library = Library()

        self.library.add_book(Book(101, "Python", "Guido"))
        self.library.add_book(Book(102, "Java", "James"))

    def display_menu(self):
        print("===== Library Management System =====")
        print("1. Display Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()

            choice = input("Enter your choice: ")

            if choice == "1":
                self.library.display_books()

            elif choice == "2":
                book_id = input("Enter Book ID: ")
                print(self.library.issue_book(book_id))

            elif choice == "3":
                book_id = input("Enter Book ID: ")
                print(self.library.return_book(book_id))

            elif choice == "4":
                print("Thank You")
                break

            else:
                print("Invalid Choice")