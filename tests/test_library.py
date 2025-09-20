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

if __name__ == "__main__":
    unittest.main()