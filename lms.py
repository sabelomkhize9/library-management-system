import datetime
import os
import json

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = {}

    def add_book(self, book):
        if book in self.books:
            print(f"The book '{book}' is already in the library.")
        else:
            self.books.append(book)
            print(f"The book '{book}' has been added to the library.")

    def view_books(self):
        print("Available Books:")
        for book in self.books:
            if book not in self.borrowed_books:
                print(f" - {book}")
        
        print("\nBorrowed Books:")
        for book, date in self.borrowed_books.items():
            print(f" - {book}, borrowed on {date.strftime('%Y-%m-%d')}")

    def borrow_book(self, book):
        if book not in self.books:
            print(f"The book '{book}' is not in the library.")
        elif book in self.borrowed_books:
            print(f"The book '{book}' is already borrowed.")
        else:
            self.borrowed_books[book] = datetime.datetime.now()
            print(f"You have borrowed '{book}'.")

    def return_book(self, book):
        if book not in self.borrowed_books:
            print(f"The book '{book}' is not borrowed.")
        else:
            borrow_date = self.borrowed_books.pop(book)
            days_borrowed = (datetime.datetime.now() - borrow_date).days

            if days_borrowed > 30:
                print(f"You are returning '{book}' {days_borrowed - 30} days late. A penalty may apply.")
            else:
                print(f"Thank you for returning '{book}' on time.")

    def delete_book(self, book):
        if book in self.books:
            self.books.remove(book)
            self.borrowed_books.pop(book, None)
            print(f"The book '{book}' has been removed from the library.")
        else:
            print(f"The book '{book}' is not in the library.")

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                data = {
                    'books': self.books,
                    'borrowed_books': {book: date.strftime('%Y-%m-%d') for book, date in self.borrowed_books.items()}
                }
                json.dump(data, file)
            print(f"Library data has been saved to {filename}.")
        except IOError:
            print(f"Failed to save data to {filename}.")

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            print(f"The file '{filename}' does not exist.")
            return
        
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.books = data['books']
                self.borrowed_books = {book: datetime.datetime.strptime(date, '%Y-%m-%d') for book, date in data['borrowed_books'].items()}
            print(f"Library data has been loaded from {filename}.")
        except (IOError, json.JSONDecodeError):
            print(f"Failed to load data from {filename}.")

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. View Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Delete a Book")
        print("6. Save Library Data")
        print("7. Load Library Data")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice (1-8): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")
            continue

        if choice == 1:
            book = input("Enter the name of the book to add: ")
            library.add_book(book)
        elif choice == 2:
            library.view_books()
        elif choice == 3:
            book = input("Enter the name of the book to borrow: ")
            library.borrow_book(book)
        elif choice == 4:
            book = input("Enter the name of the book to return: ")
            library.return_book(book)
        elif choice == 5:
            book = input("Enter the name of the book to delete: ")
            library.delete_book(book)
        elif choice == 6:
            filename = input("Enter the filename to save the library data: ")
            library.save_to_file(filename)
        elif choice == 7:
            filename = input("Enter the filename to load the library data: ")
            library.load_from_file(filename)
        elif choice == 8:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()

