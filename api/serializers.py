from uuid import uuid4
from rest_framework import serializers
from storeapp.models import Category,Product,Cartitems,Cart
from rest_framework.exceptions import ValidationError


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    category = CategorySerializer()