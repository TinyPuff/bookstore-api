from rest_framework import viewsets
from rest_framework import permissions
from .models import Book, Category, Review
from .serializers import BookSerializer, CategorySerializer, ReviewSerializer

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
