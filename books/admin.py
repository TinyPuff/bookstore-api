from django.contrib import admin
from .models import Book, Category

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ("title", "author", "price", "stock")


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
