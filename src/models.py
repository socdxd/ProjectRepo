from datetime import datetime, timedelta
from typing import List, Optional

class Book:
    def __init__(self, isbn: str, title: str, author: str, year: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True
        self.borrowed_by: Optional[str] = None
        self.due_date: Optional[datetime] = None

class Member:
    def __init__(self, member_id: str, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books: List[str] = []
        self.registration_date = datetime.now()

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.loan_period_days = 14

    def add_book(self, book: Book):
        self.books[book.isbn] = book

    def add_member(self, member: Member):
        self.members[member.member_id] = member

    def borrow_book(self, isbn: str, member_id: str) -> bool:
        if isbn not in self.books or member_id not in self.members:
            return False

        book = self.books[isbn]
        member = self.members[member_id]

        if not book.is_available:
            return False

        book.is_available = False
        book.borrowed_by = member_id
        book.due_date = datetime.now() + timedelta(days=self.loan_period_days)
        member.borrowed_books.append(isbn)
        return True

    def return_book(self, isbn: str) -> bool:
        if isbn not in self.books:
            return False

        book = self.books[isbn]
        if book.is_available:
            return False

        member = self.members[book.borrowed_by]
        member.borrowed_books.remove(isbn)

        book.is_available = True
        book.borrowed_by = None
        book.due_date = None
        return True

    def get_overdue_books(self) -> List[Book]:
        overdue = []
        current_time = datetime.now()

        for book in self.books.values():
            if not book.is_available and book.due_date < current_time:
                overdue.append(book)

        return overdue

    def search_books_by_author(self, author: str) -> List[Book]:
        """Search for books by author name (case-insensitive)"""
        author_lower = author.lower()
        matching_books = []
        
        for book in self.books.values():
            if author_lower in book.author.lower():
                matching_books.append(book)
        
        return matching_books

    def get_member_borrowed_books(self, member_id: str) -> List[Book]:
        """Get all books currently borrowed by a member"""
        if member_id not in self.members:
            return []
        
        member = self.members[member_id]
        borrowed_books = []
        
        for isbn in member.borrowed_books:
            if isbn in self.books:
                borrowed_books.append(self.books[isbn])
        
        return borrowed_books