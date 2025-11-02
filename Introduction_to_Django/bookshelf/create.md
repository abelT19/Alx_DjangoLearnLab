Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
 ["Book.objects.create", "title", "author", "George Orwell"]
from bookshelf.models import Book

# Create a new Book object
Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
