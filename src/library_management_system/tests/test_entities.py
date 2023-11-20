from entities import *
import unittest

class BookTests(unittest.TestCase):
    def test_init(self):
        name = "Think Faster, Talk Smarter: How to Speak Successfully When You're Put on the Spot"
        year = 2023

        book = Book(
            name,
            year,
            Author("Matt Abrahams"))
        
        self.assertEqual(book.name, name)
        self.assertEqual(book.year, year)

class AuthorTests(unittest.TestCase):
    def test_init(self):
        name = "Matt Abrahams"

        author = Author(name)

        self.assertEqual(author.name, name)

class LibraryTests(unittest.TestCase):
    def test_init(self):
        name = "Think Faster, Talk Smarter: How to Speak Successfully When You're Put on the Spot"
        year = 2023
        book = Book(
            name,
            year,
            [Author("Matt Abrahams")])
        
        library = Library([book])

        for key in library.books.keys():
            self.assertEqual(library.books[key].name, book.name)

    def test_add_book(self):
        library = Library([])
        name = "Think Faster, Talk Smarter: How to Speak Successfully When You're Put on the Spot"
        year = 2023
        book = Book(
            name,
            year,
            [Author("Matt Abrahams")])
        
        library.add_book(book)

        self.assertEqual(len(library.books), 1)
        for key in library.books.keys():
            self.assertEqual(library.books[key].name, book.name)

    def test_remove_book(self):
        name = "Think Faster, Talk Smarter: How to Speak Successfully When You're Put on the Spot"
        year = 2023
        book = Book(
            name,
            year,
            [Author("Matt Abrahams")])
        
        library = Library([book])

        keys = [key for key in library.books.keys()]
        for key in keys:
            library.remove_book(key)
        self.assertEqual(len(library.books), 0)

if __name__ == "__main__":
    unittest.main()
