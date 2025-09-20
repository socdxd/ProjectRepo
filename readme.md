# Library Management System

A comprehensive Python library management system that handles book cataloging, member management, borrowing operations, and advanced search functionality.

## Features

- Book management (add, track availability)
- Member registration and management
- Book borrowing and return system
- Overdue book tracking
- 14-day loan period
- Search books by author (case-insensitive)
- Track member's borrowed books
- Comprehensive test coverage
- Full API documentation

## Quick Start

### Installation

```bash
git clone https://github.com/socdxd/ProjectRepo
cd ProjectRepo
```

### Usage Example

```python
from src.models import Library, Book, Member

# Initialize library
library = Library()

# Add book
book = Book("978-0-123456-78-9", "Python Programming", "John Smith", 2023)
library.add_book(book)

# Register member
member = Member("M001", "Jane Doe", "jane@example.com")
library.add_member(member)

# Borrow book
success = library.borrow_book("978-0-123456-78-9", "M001")
print(f"Borrow successful: {success}")

# Return book
returned = library.return_book("978-0-123456-78-9")
print(f"Return successful: {returned}")

# Search books by author
john_books = library.search_books_by_author("John Smith")
print(f"Books by John Smith: {len(john_books)}")

# Get member's borrowed books
borrowed = library.get_member_borrowed_books("M001")
print(f"Member has {len(borrowed)} borrowed books")
```

### Running Tests

```bash
python -m pytest tests/
```

or

```bash
python tests/test_library.py
```

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request