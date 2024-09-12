from rest_framework.routers import SimpleRouter
from .views import CartViewSet, UserCartView
from django.urls import path


router = SimpleRouter()
router.register("cart", CartViewSet, basename="cart")

urlpatterns = [
    path("cart/users/<int:user_id>/", UserCartView.as_view(), name="user_cart"),
] + router.urls
