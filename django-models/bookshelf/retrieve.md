# Retrieve Book Instance

**Command:**

```python
from bookshelf.models import Book

# Retrieve a specific book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
print(book.title, book.author, book.publication_year)


Output:
1984 George Orwell 1949
