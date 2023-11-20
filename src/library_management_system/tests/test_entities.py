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

if __name__ == "__main__":
    unittest.main()
