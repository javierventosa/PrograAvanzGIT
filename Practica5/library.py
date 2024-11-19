from book import Book

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    def remove_book(self, isbn: str):
        self._books = [book for book in self._books if book.isbn != isbn]

    def borrow_book(self, isbn: str):
        for book in self._books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                return True
        return False

    def return_book(self, isbn: str):
        for book in self._books:
            if book.isbn == isbn and book.is_borrowed:
                book.is_borrowed = False
                return True
        return False

    def search_books(self, keyword: str):
        return [book for book in self._books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]

    def show_books(self):
        return "\n".join(str(book) for book in self._books)
