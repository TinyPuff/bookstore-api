from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()


class CartViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):  # Prevents the creation of duplicates
        email = EmailAddress.objects.get(email=request.data.get("user"))
        product = int(request.data.get("product"))
        cart = Cart.objects.filter(user=email, product=product)

        if cart.count() > 0:
            return Response(
                {"detail": "Product is already in the cart!"},
                status.HTTP_400_BAD_REQUEST,
            )

        return super().create(request, *args, **kwargs)


class UserCartView(generics.ListCreateAPIView):
    """Lists all cart items belonging to a specific user based on the passed user_id in the url"""

    permission_classes = (permissions.IsAdminUser,)
    serializer_class = CartSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        user = User.objects.get(id=int(user_id))
        return Cart.objects.filter(user=EmailAddress.objects.get(email=user.email))
