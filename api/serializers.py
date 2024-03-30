from uuid import uuid4
from rest_framework import serializers
from storeapp.models import Category,Product,Cartitems,Cart,Review
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


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','name','description','date_created']

    def create(self, validated_data):
        validated_data['product_id'] = self.context['product_id']
        return Review.objects.create(**validated_data)
    
class CartSerializer(serializers.ModelSerializer):
    cart_id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Cart
        fields = ['cart_id','items']

class CartitemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartitems
        fields = ['id','cart','product','quantity']
