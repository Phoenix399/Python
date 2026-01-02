class Library:
    def __init__(self, list_of_books, name):
        self.books = list_of_books
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have the following books in our library {self.name}:")
        for book in self.books:
            print(book)

    def lendBook(self, user, book):
        if book not in self.books:
            print("This book is not available in our library.")
        elif book in self.lendDict:
            print(f"Sorry, this book is already lent to {self.lendDict[book]}.")
        else:
            self.lendDict[book] = user
            print("Lender-Book database has been updated. You can take the book now.")

    def addBook(self, book):
        self.books.append(book)
        print(f"{book} has been added to the book list.")

    def returnBook(self, book):
        if book in self.lendDict:
            self.lendDict.pop(book)
            print(f"{book} has been returned.")
        else:
            print("This book was not lent from our library.")


books = Library(
    ['Python Crash Course', 'Automate the Boring Stuff with Python', 'Learn Java in One Day',
     'C++ for Beginners', 'Clean Code', 'Rich Dad Poor Dad', 'The 7 Habits of Highly Effective People',
     'Think and Grow Rich', 'Atomic Habits', 'A Brief History of Time', 'The Selfish Gene', 'Cosmos',
     'Harry Potter and the Sorcerer’s Stone', 'To Kill a Mockingbird', 'The Hobbit', 'The Alchemist',
     'The Diary of a Young Girl', 'Long Walk to Freedom', 'Sapiens: A Brief History of Humankind'],
    "Phoenix Library"
)

user_name = input("Welcome to the library! Please enter your name: ")

while True:
    print(f"\nHello {user_name}, welcome to the {books.name} library. Please choose an option:")
    print("1. Display all books")
    print("2. Lend a book")
    print("3. Add a book")
    print("4. Return a book")
    user_choice = input("Enter your choice (1-4) or 'q' to quit: ")

    if user_choice == 'q':
        print("Thank you for using the library. Goodbye!")
        break
    elif user_choice == '1':
        books.displayBooks()
    elif user_choice == '2':
        book = input("Enter the name of the book you want to lend: ")
        books.lendBook(user_name, book)
    elif user_choice == '3':
        book = input("Enter the name of the book you want to add: ")
        books.addBook(book)
    elif user_choice == '4':
        book = input("Enter the name of the book you want to return: ")
        books.returnBook(book)

