from typing import List

class Library():
    """Represents a library in the library management system
    Libraries contain books
    
    Attributes:
        books (List[Book]): Books that library holds
    """

    def __init__(self, books):
        self.books = books

class Book():
    """Represents a book in the library management system
    Books have authors

    Attributes:
        name (str): Name of the book
        year (int): Year it was written
        authors (List[Author]): Authors of the book
    """

    def __init__(self, name, year, authors):
        self.name = name
        self.year = year
        self.authors = authors

class Author():
    """Represents author of a book in the library management system

    Attributes:
        name (str): Name of author
        year (int): Author's year of birth
    """

    def __init__(self, name, year=None):
        self.name = name
        self.year = year

