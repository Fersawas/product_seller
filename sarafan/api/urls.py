from django.urls import include, path
from djoser.views import TokenCreateView, TokenDestroyView

from rest_framework import routers

from djoser.views import UserViewSet

from api.views import (CategoryViewSet, SubCategoryViewSet,
                       ProductViewSet, ShopCartViewSet)

router = routers.SimpleRouter()
#
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'sub_category', SubCategoryViewSet, basename='sub_category')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:pk>/shopping_cart/',
         ShopCartViewSet.as_view({'post': 'shopping_cart',
                                  'delete': 'shopping_cart'})),
    path('shopping_cart/', ShopCartViewSet.as_view(
        {'get': 'view_shopping_cart'}
    )),
    path('remove_shopping_cart/', ShopCartViewSet.as_view(
        {'delete': 'removing_shopping_cart'}
    )),
    path('login/', TokenCreateView.as_view()),
    path('logout/', TokenDestroyView.as_view())
]
