from rest_framework import serializers
from .models import Book, Category


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
