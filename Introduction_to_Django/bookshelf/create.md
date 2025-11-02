from bookshelf.models import Book
 ["Book.objects.create", "title", "author", "George Orwell"]
# Create a new Book object
book1 = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Verify the object was created
print(book1)

