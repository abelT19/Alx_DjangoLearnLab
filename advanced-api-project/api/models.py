from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Author(models.Model):
    """
    Represents a book author.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book written by an author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'  # Allows reverse access: author.books.all()
    )

    def clean(self):
        """
        Custom validation to ensure publication_year is not in the future.
        """
        current_year = date.today().year
        if self.publication_year > current_year:
            raise ValidationError('Publication year cannot be in the future.')

    def __str__(self):
        return self.title
