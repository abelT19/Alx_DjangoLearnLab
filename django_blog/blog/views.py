from rest_framework import viewsets
from rest_framework import permissions
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

"POST", "method", "save()"
# Book ViewSet
# -----------------------------
class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Change to IsAuthenticated if needed


# -----------------------------
# Author ViewSet
# -----------------------------
class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Authors to be viewed or edited.
    Includes nested Book data automatically.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]  # Change to IsAuthenticated if needed

