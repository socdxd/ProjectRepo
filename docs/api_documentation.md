# API Documentation

## Library Management System API

### Classes

#### Book
Represents a book in the library system.

**Attributes:**
- `isbn` (str): Unique identifier for the book
- `title` (str): Book title
- `author` (str): Book author
- `year` (int): Publication year
- `is_available` (bool): Availability status
- `borrowed_by` (str, optional): Member ID who borrowed the book
- `due_date` (datetime, optional): Return due date

#### Member
Represents a library member.

**Attributes:**
- `member_id` (str): Unique member identifier
- `name` (str): Member full name
- `email` (str): Contact email
- `borrowed_books` (List[str]): List of borrowed book ISBNs
- `registration_date` (datetime): Registration timestamp

#### Library
Main library management class.

**Methods:**

##### `add_book(book: Book) -> None`
Adds a new book to the library collection.

##### `add_member(member: Member) -> None`
Registers a new library member.

##### `borrow_book(isbn: str, member_id: str) -> bool`
Processes book borrowing transaction.

**Returns:** `True` if successful, `False` if book unavailable or invalid IDs.

##### `return_book(isbn: str) -> bool`
Processes book return transaction.

**Returns:** `True` if successful, `False` if book not borrowed.

##### `get_overdue_books() -> List[Book]`
Retrieves list of overdue books.

**Returns:** List of Book objects past due date.

### Configuration

- Default loan period: 14 days
- Overdue calculation: Based on current system time
- Member capacity: Unlimited
- Book duplicates: Not supported (unique ISBN required)