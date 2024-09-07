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

