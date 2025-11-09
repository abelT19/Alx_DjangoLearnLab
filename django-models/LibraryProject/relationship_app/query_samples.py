["Author.objects.get(name=author_name)", "objects.filter(author=author)"]
["Library.objects.get(name=library_name)"]
# Import Django setup
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Query 1: All books by a specific author ---
author = Author.objects.get(name="J.K. Rowling")
books_by_author = author.books.all()
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

# --- Query 2: List all books in a library ---
library = Library.objects.get(name="Central Library")
library_books = library.books.all()
print(f"Books in {library.name}: {[book.title for book in library_books]}")

# --- Query 3: Retrieve the librarian for a library ---
librarian = library.librarian
print(f"Librarian of {library.name}: {librarian.name}")


