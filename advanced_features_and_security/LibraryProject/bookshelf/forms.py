from django import forms
from .models import Book  # Replace with your actual model

# Example form for adding or updating a book
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # Your model here
        fields = ['title', 'author', 'published_date']  # Adjust fields as needed
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
