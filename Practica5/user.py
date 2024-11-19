class User:
    def __init__(self, name: str, user_id: str):
        self._name = name
        self._user_id = user_id
        self._borrowed_books = []

    @property
    def name(self):
        return self._name

    @property
    def user_id(self):
        return self._user_id

    @property
    def borrowed_books(self):
        return self._borrowed_books

    def borrow_book(self, book):
        self._borrowed_books.append(book)

    def return_book(self, isbn: str):
        self._borrowed_books = [book for book in self._borrowed_books if book.isbn != isbn]

    def __str__(self):
        books_list = ", ".join(book.title for book in self._borrowed_books)
        return f"Nombre: {self._name}, ID: {self._user_id}, Libros prestados: {books_list}"
