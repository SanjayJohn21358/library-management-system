from entities import *

if __name__ == "__main__":
    library = Library([
        Book(
            name="Harry Potter and the Order of the Phoenix",
            year=2003,
            authors=[Author("J.K. Rowling")]
        ),
        Book(
            name="Breaking Dawn",
            year=2008,
            authors=[Author("Stephenie Meyer")]
        ),
        Book(
            name="Design Patterns: Elements of Reusable Object-Oriented Software",
            year=1994,
            authors=[
                Author("Erick Gamma"),
                Author("Richard Helm"),
                Author("Ralph Johnson"),
                Author("John Vlissides")
            ]
        )
    ])
