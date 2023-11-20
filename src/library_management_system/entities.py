from typing import List
import uuid

class Author():
    """Represents author of a book in the library management system

    Attributes:
        name (str): Name of author
        year (int): Author's year of birth
    """

    def __init__(self, name: str, year: int=None):
        self.name = name
        self.year = year

class Book():
    """Represents a book in the library management system
    Books have authors

    Attributes:
        name (str): Name of the book
        year (int): Year it was written
        authors (List[Author]): Authors of the book
    """

    def __init__(self, name: str, year: int, authors: List[Author]):
        self.name = name
        self.year = year
        self.authors = authors

class Library():
    """Represents a library in the library management system
    Libraries contain books
    
    Arguments:
        - books (List[Book]): Books to initialize library with

    Attributes:
        - books (Dictionary[Book]): Books that library holds
    """

    def __init__(self, books: List[Book]):
        self.books = {}
        for book in books:
            unique_id = self.get_unique_id()
            self.books[unique_id] = book
            self.display_book_information(unique_id)

    def add_book(self, book: Book):
        """Add book to library
        Adds book to self.books

        Arguments:
            - book (Book): Book to add to library

        Returns:
            Unique ID assigned to book
        """
        unique_id = self.get_unique_id()
        self.books[unique_id] = book

        return unique_id

    def remove_book(self, unique_id: str):
        """Remove book from library by unique id
        Removes book from self.books

        Arguments:
            - unique_id (str): Unique id assigned to book when added to library
        """

        del self.books[unique_id]

    def get_unique_id(self) -> str:
        """Get unique id to use in library

        Returns:
            Unique ID that is a string
        """
        unique_id = ""
        while not unique_id or unique_id in self.books:
            unique_id = str(uuid.uuid4())
        return unique_id

    def display_book_information(self, unique_id: str):
        """Display information about book
        Prints info about book to stdout

        Arguments:
            - unique_id (str): Unique id assigned to book when added to library
        """
        if unique_id not in self.books:
            print(f"Book with id: {unique_id} does not exist in library!")
        else:
            book = self.books[unique_id]
            print("---------------------------")
            print(f"ID: {unique_id}")
            print(f"Name: \'{book.name}\'")
            print(f"Year: {book.year}")
            for index, author in enumerate(book.authors, 1):
                print(f"Author #{index} name: {author.name}")
            print("---------------------------")

