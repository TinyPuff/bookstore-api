from rest_framework import serializers
from .models import Book, Category, Review
from django.contrib.auth import get_user_model


User = get_user_model()


class BookSerializer(serializers.ModelSerializer):
    primary_category = serializers.StringRelatedField(many=True)
    secondary_category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "author",
            "price",
            "stock",
            "primary_category",
            "secondary_category",
            "reviews",
        )


class CategorySerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(
        many=True, queryset=Book.objects.all(), slug_field="title"
    )

    class Meta:
        model = Category
        fields = (
            "title",
            "books",
        )


class ReviewSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(queryset=Book.objects.all(), slug_field="title")
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="email"
    )

    class Meta:
        model = Review
        fields = (
            "id",
            "book",
            "author",
            "review",
        )
