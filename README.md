# library-management-system
A small python program designed to emulate a library management system, prompted by ChatGPT

## Problem statement # 1
Me: Help me generate a good problem to solve with some python code, preferably so that I can demonstrate object oriented programming principles, file opening and reading, and other design principles

ChatGPT: 
Certainly! Let's create a simple problem that involves managing a library system. You can demonstrate object-oriented programming (OOP) principles, file opening and reading, and other design principles through this example.

### Problem: Library Management System

Imagine you are tasked with creating a library management system where you need to keep track of books, authors, and library patrons. The system should support the following functionalities:


#### Book Management:

1. Add a new book to the library.
1. Remove a book from the library.
1. Display information about a specific book.

#### Author Management:

1. Add a new author to the system.
1. Remove an author (and associated books) from the system.
1. Display information about a specific author.

#### Patron Management:

1. Add a new patron to the library.
1. Remove a patron from the library.
1. Display information about a specific patron.

#### Borrowing and Returning:

1. Allow patrons to borrow and return books.
1. Keep track of the due date for borrowed books.

#### File Handling:

1. Save the library information to a file.
1. Load the library information from a file.

## Solutions & Methodologies
- Represent each entity as a class
- Follow test driven development
- Save state in files (consider each csv file a table in a database)

### Project Development

This readme will also serve as our demonstration of project tracking and development in lieu of better resources like Jira, ClickUp, etc.
We will break the tasks down into small units of work, and expect our project to be built with them step by step.
A pull request should encapsulate each unit of work, though we may have more than one PR for a given task

Tasks:
1. Write README
2. Sketch Book, Author and Library class and tests, implement Library->Book functionality
3. Write Author class and tests
4. Write Patron class and tests
5. Write Borrowing and Returning functionality
6. Implement saving and loading state in files

