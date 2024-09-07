# Create a Book Instance

Command:
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

Output:

<Book: 1984>

# Delete Book Instance
**Command:**

```python
from bookshelf.models import Book

# Retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Verify deletion
remaining_books = Book.objects.all()
print(remaining_books)

Output:
<QuerySet []>


**Command:**

```python
from bookshelf.models import Book
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)

Output:
1984 George Orwell 1949

# Retrieve Book Instance

**Command:**

```python
from bookshelf.models import Book

# Retrieve a specific book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
print(book.title, book.author, book.publication_year)

# Retrieve the book to update
book = Book.objects.get(title="1984")

# Update the book's title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print(updated_book.title, updated_book.author, updated_book.publication_year)

Output:
Nineteen Eighty-Four George Orwell 1949




