from rest_framework import viewsets
from rest_framework import permissions
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
