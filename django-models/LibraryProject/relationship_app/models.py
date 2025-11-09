import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Query 1: All books by a specific author ---
author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
books_by_author = author.books.all()
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

# --- Query 2: List all books in a library dynamically ---
library_name = "Central Library"  # Change this variable as needed
library = Library.objects.get(name=library_name)
library_books = library.books.all()
print(f"Books in {library.name}: {[book.title for book in library_books]}")

# --- Query 3: Retrieve the librarian for a library dynamically ---
librarian = library.librarian
print(f"Librarian of {library.name}: {librarian.name}")
