from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


from products.models import Category, SubCategory, Product
from users.models import ShopCart
from api.serializers import (
    CategorySerializer,
    SubCategorySerializer,
    ProductSerializer,
    MainShopCartSerializer,
)
from products.constants import (PRDOCUT_ERROR, PRODUCT_CONFIRM,
                                SHOPPING_CART_ERROR)


User = get_user_model()


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        AllowAny,
    ]
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubCategory.objects.all()
    permission_classes = [
        AllowAny,
    ]
    serializer_class = SubCategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        AllowAny,
    ]
    serializer_class = ProductSerializer


class ShopCartViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == "view_shopping_cart":
            return MainShopCartSerializer

    @action(["post", "delete"], detail=True)
    def shopping_cart(self, request, pk, *args, **kwagrs):
        user = request.user
        user = get_object_or_404(User, username=user.username)
        try:
            product = Product.objects.get(pk=pk)
        except Exception:
            return Response(
                {"ERROR": PRDOCUT_ERROR["no product"]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if request.method == "DELETE":
            try:
                product_in_shopcart = ShopCart.objects.filter(
                    user=user, product=product
                ).first()
            except Exception:
                return Response(
                    {"ERROR": PRDOCUT_ERROR["not in shopcart"]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            product_in_shopcart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        ShopCart.objects.create(user=user, product=product)
        return Response(
            {"DONE": PRODUCT_CONFIRM["product add"]},
            status=status.HTTP_201_CREATED
        )

    @action("delete", detail=False)
    def removing_shopping_cart(self, request, *args, **kwargs):
        user = request.user
        user = get_object_or_404(User, username=user.username)
        shop_cart = ShopCart.objects.filter(user=user)
        if shop_cart.exists():
            shop_cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"ERROR": SHOPPING_CART_ERROR["empty"]},
            status=status.HTTP_400_BAD_REQUEST
        )

    @action("get", detail=False)
    def view_shopping_cart(self, request, *args, **kwargs):
        user = request.user
        user = get_object_or_404(User, username=user.username)
        serializer = self.get_serializer(user)
        return Response(serializer.data)
