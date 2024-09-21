# Update Book Title

**Command:**

```python
from bookshelf.models import Book

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
