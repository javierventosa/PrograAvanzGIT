class Book:
    def __init__(self, title : str, author: str, ISBN: str):
        self.__title = title
        self.__author = author
        self.__ISBN = ISBN
        self._is_borrowed = False

    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author
    
    @property
    def ISBN(self):
        return self.__ISBN

    @property
    def is_borrowed(self):
        return self._is_borrowed

    @is_borrowed.setter
    def is_borrowed(self, value: bool):
        self._is_borrowed = value

    def __str__(self):
        estado_str = "Prestado" if self._is_borrowed else "Disponible"
        return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__ISBN}, Estado: {estado_str}"