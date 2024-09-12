from django.contrib import admin
from .models import Book, Category, Review

# Register your models here.


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class BookAdmin(admin.ModelAdmin):
    model = Book
    inlines = [
        ReviewInline,
    ]
    list_display = ("title", "author", "price", "stock")


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fields = ("title",)


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
