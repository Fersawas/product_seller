import base64

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.db.models import Count, Sum

from rest_framework import serializers

from products.models import Category, SubCategory, Product
from users.models import ShopCart


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class CategorySerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    sub_categories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'slug',
            'image',
            'sub_categories'
        ]

    def get_sub_categories(self, obj):
        sub_category = SubCategory.objects.filter(category=obj)
        return SubCategorySerializer(sub_category, many=True).data


class SubCategorySerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    category = serializers.SlugRelatedField(
        slug_field='slug',
        read_only=True
    )

    class Meta:
        model = SubCategory
        fields = [
            'id',
            'title',
            'slug',
            'image',
            'category'
        ]


class ProductSerializer(serializers.ModelSerializer):
    small_image = Base64ImageField()
    medium_image = Base64ImageField()
    big_image = Base64ImageField()
    sub_category = serializers.SlugRelatedField(
        slug_field='slug',
        read_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'slug',
            'small_image',
            'medium_image',
            'big_image',
            'sub_category',
            'price'
        ]


class ShopCartSerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField()
    product_sum = serializers.IntegerField()
    category = serializers.CharField(source='sub_category.category')
    sub_category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'slug',
            'small_image',
            'product_count',
            'product_sum',
            'sub_category',
            'category'
        ]


class MainShopCartSerializer(serializers.Serializer):
    products = serializers.SerializerMethodField()
    all_summ = serializers.SerializerMethodField()

    class Meta:
        model = ShopCart
        fields = [
            'products',
            'all_summ'
        ]

    def get_all_summ(self, obj=None, **kwargs):
        shop_cart = Product.objects.filter(
            shopcart__user=self.context['request'].user
            ).aggregate(total_sum=Sum('price'))
        return shop_cart['total_sum']

    def get_products(self, obj):
        shop_cart = Product.objects.filter(
            shopcart__user=self.context['request'].user
            ).annotate(product_count=Count('slug'), product_sum=Sum('price'))
        return ShopCartSerializer(shop_cart, many=True).data
