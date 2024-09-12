from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from allauth.account.models import EmailAddress

# Create your views here.


class CartViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        email = EmailAddress.objects.get(email=request.data.get("user"))
        product = int(request.data.get("product"))
        cart = Cart.objects.filter(user=email, product=product)

        if cart.count() > 0:
            return Response(
                {"detail": "Product is already in the cart!"},
                status.HTTP_400_BAD_REQUEST,
            )

        return super().create(request, *args, **kwargs)
