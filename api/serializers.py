from uuid import uuid4
from rest_framework import serializers
from storeapp.models import Category,Product,Cartitems,Cart,Review,ProductImage
from rest_framework.exceptions import ValidationError


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id','product','image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many = True, read_only = True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length = 1000000, allow_empty_file = False, use_url = False), write_only = True
    )
    class Meta:
        model = Product
        fields = ['id','name','description','inventory','price','images','uploaded_images']

    def create(self,validated_data):
        uploaded_images = validated_data.pop('uploaded_images')
        product = Product.objects.create(**validated_data)
        for image in uploaded_images:
            new_product_image = ProductImage.objects.create(product=product,image=image)

        return product    



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','name','description','date_created']

    def create(self, validated_data):
        validated_data['product_id'] = self.context['product_id']

        return Review.objects.create(**validated_data)
    


class CartitemsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','price']

class CartitemsSerializer(serializers.ModelSerializer):
    product = CartitemsProductSerializer(many=False)
    class Meta:
        model = Cartitems
        fields = ['id','product','quantity','subTotal']
    
class CartSerializer(serializers.ModelSerializer):
    cart_id = serializers.UUIDField(read_only=True)
    items = CartitemsSerializer(many=True,read_only = True)
    # cart_total = serializers.SerializerMethodField(method_name='main_total')
    class Meta:
        model = Cart
        fields = ['cart_id','items','cart_total']


    # def main_total(self, cart:Cart):
    #     items = cart.items.all()
    #     return sum([item.quantity * item.product.price for item in items])    


