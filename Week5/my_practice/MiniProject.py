# Mini Project – Library Management System

# A system with classes Book, Member, Library.

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.available = True

class Member:
  def __init__(self, name):
    self.name = name
    self.borrowed = []

class Library:
  def __init__(self):
    self.books = []
    
  def add_book(self, book):
    self.books.append(book)
    
  def borrow_book(self, member, title):
    for book in self.books:
      if book.title == title and book.available:
        book.available = False
        member.borrowed.append(book)
        print(f"{member.name} borrowed {title}")
        return
      print('Book not available.')
