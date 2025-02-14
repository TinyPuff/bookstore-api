from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    cover = models.ImageField(upload_to="covers/", blank=True)
    title = models.CharField(max_length=350)
    author = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    details = models.TextField(max_length=1000, default="")
    stock = models.PositiveIntegerField(default=0)
    primary_category = models.ManyToManyField(Category, related_name="books")
    secondary_category = models.ManyToManyField(
        Category, related_name="sbooks", blank=True
    )

    class Meta:
        indexes = [models.Index(fields=["id"], name="id_index")]

    def __str__(self):
        return f"{self.author} - {self.title}"


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.CharField(max_length=250)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review[:50]
