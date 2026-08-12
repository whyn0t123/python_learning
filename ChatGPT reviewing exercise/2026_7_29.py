from pathlib import Path

class Book:
    def __init__(self, title, author, year, is_borrowed=False):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = is_borrowed

    def display(self):
        if self.is_borrowed == False:
            return f"{self.title} - {self.author.title()} ({self.year}) [Available]"
        
        elif self.is_borrowed == True:
            return f"{self.title} - {self.author.title()} ({self.year}) [Borrowed]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book.display()}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed == False:
                    print(f"You borrowed {title}.")
                    book.is_borrowed = True

                elif book.is_borrowed == True:
                    print("Sorry, this book is already borrowed.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"You returned {title}.")
                else:
                    print("This book is not borrowed.")
                return

        print("Book not found.")

    def save_to_file(self, filename):
        path = Path(filename)

        contents = ''

        for book in self.books:
            contents += (
                f"{book.title},"
                f"{book.author},"
                f"{book.year},"
                f"{book.is_borrowed}\n"
            )

        path.write_text(contents,encoding="utf-8")

        print("Books saved.")

    def load_books(filename):
        path = Path(filename)

        books = []

        try:
            contents = path.read_text(encoding="utf-8")

        except FileNotFoundError:
            print("File not found.")
            return books

        lines = contents.splitlines()

        for line in lines:
            title, author, year, is_borrowed = line.split(",")

            book = Book(
                title,
                author,
                int(year),
                is_borrowed == "True"
            )

            books.append(book)

        return books

library = Library()

book1 = Book("Python编程", "Eric Matthes", 2023)
book2 = Book("C语言程序设计", "谭浩强", 2020)

library.add_book(book1)
library.add_book(book2)


print("所有书籍：")
library.show_books()


print("\n借书：")
library.borrow_book("Python编程")


print("\n当前状态：")
library.show_books()


print("\n保存文件：")
library.save_to_file("books.txt")


print("\n从文件读取：")

new_books = Library.load_books("books.txt")

for book in new_books:
    print(book.display())