from rest_framework import serializers
from .models import Cart
from books.models import Book
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress


User = get_user_model()


class CartSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=EmailAddress.objects.all(), slug_field="email"
    )

    class Meta:
        model = Cart
        fields = (
            "id",
            "user",
            "product",
            "quantity",
        )

    def validate_product(
        self, data
    ):  # Checks whether the quantity exceeds the amount in stock
        quantity = int(self.initial_data["quantity"])
        stock = int(Book.objects.get(id=data.id).stock)
        if quantity > stock:
            if stock == 1:
                msg = f"There is only {stock} in stock."
            elif stock > 1:
                msg = f"There are only {stock} in stock."
            elif stock == 0:
                msg = "There is none in stock."
            raise serializers.ValidationError(msg)
        return data

    def to_representation(
        self, instance
    ):  # Adds two additional values to the json response. (user_id and product_title)
        representation = super().to_representation(instance)
        representation["product_title"] = str(instance.product)
        representation["user_id"] = User.objects.get(email=instance.user).id
        ordered_representation = {
            "id": representation["id"],
            "user": representation["user"],
            "user_id": representation["user_id"],
            "product": representation["product"],
            "product_title": representation["product_title"],
            "quantity": representation["quantity"],
        }
        return ordered_representation
