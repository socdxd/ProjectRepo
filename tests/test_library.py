import unittest
from datetime import datetime, timedelta
from src.models import Book, Member, Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("978-0-123456-78-9", "Test Book", "Test Author", 2023)
        self.member = Member("M001", "John Doe", "john@example.com")

    def test_add_book(self):
        self.library.add_book(self.book)
        self.assertIn(self.book.isbn, self.library.books)

    def test_add_member(self):
        self.library.add_member(self.member)
        self.assertIn(self.member.member_id, self.library.members)

    def test_borrow_book_success(self):
        self.library.add_book(self.book)
        self.library.add_member(self.member)

        result = self.library.borrow_book(self.book.isbn, self.member.member_id)

        self.assertTrue(result)
        self.assertFalse(self.book.is_available)
        self.assertEqual(self.book.borrowed_by, self.member.member_id)
        self.assertIn(self.book.isbn, self.member.borrowed_books)

    def test_borrow_unavailable_book(self):
        self.library.add_book(self.book)
        self.library.add_member(self.member)

        self.book.is_available = False
        result = self.library.borrow_book(self.book.isbn, self.member.member_id)

        self.assertFalse(result)

    def test_return_book(self):
        self.library.add_book(self.book)
        self.library.add_member(self.member)
        self.library.borrow_book(self.book.isbn, self.member.member_id)

        result = self.library.return_book(self.book.isbn)

        self.assertTrue(result)
        self.assertTrue(self.book.is_available)
        self.assertIsNone(self.book.borrowed_by)
        self.assertNotIn(self.book.isbn, self.member.borrowed_books)

    def test_overdue_books(self):
        self.library.add_book(self.book)
        self.library.add_member(self.member)
        self.library.borrow_book(self.book.isbn, self.member.member_id)

        self.book.due_date = datetime.now() - timedelta(days=1)
        overdue = self.library.get_overdue_books()

        self.assertEqual(len(overdue), 1)
        self.assertEqual(overdue[0].isbn, self.book.isbn)

    def test_search_books_by_author(self):
        book1 = Book("978-0-123456-78-9", "Python Basics", "John Smith", 2023)
        book2 = Book("978-0-123456-79-0", "Advanced Python", "Jane Doe", 2023)
        book3 = Book("978-0-123456-80-0", "Python Cookbook", "John Smith", 2022)
        
        self.library.add_book(book1)
        self.library.add_book(book2)
        self.library.add_book(book3)
        
        # Test case-insensitive search
        john_books = self.library.search_books_by_author("john")
        self.assertEqual(len(john_books), 2)
        
        jane_books = self.library.search_books_by_author("JANE")
        self.assertEqual(len(jane_books), 1)
        self.assertEqual(jane_books[0].title, "Advanced Python")

    def test_get_member_borrowed_books(self):
        book1 = Book("978-0-123456-78-9", "Book 1", "Author 1", 2023)
        book2 = Book("978-0-123456-79-0", "Book 2", "Author 2", 2023)
        
        self.library.add_book(book1)
        self.library.add_book(book2)
        self.library.add_member(self.member)
        
        # Borrow both books
        self.library.borrow_book(book1.isbn, self.member.member_id)
        self.library.borrow_book(book2.isbn, self.member.member_id)
        
        borrowed_books = self.library.get_member_borrowed_books(self.member.member_id)
        self.assertEqual(len(borrowed_books), 2)
        
        # Test with non-existent member
        non_existent_books = self.library.get_member_borrowed_books("NONEXISTENT")
        self.assertEqual(len(non_existent_books), 0)

if __name__ == "__main__":
    unittest.main()