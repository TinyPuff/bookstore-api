from rest_framework import viewsets
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
