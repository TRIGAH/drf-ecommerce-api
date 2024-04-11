from uuid import uuid4
from rest_framework import serializers
from storeapp.models import *
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
    


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','price']

class CartitemsSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer(many=False)
    class Meta:
        model = Cartitems
        fields = ['id','product','quantity','subTotal']

class AddCartitemsSerializer(serializers.ModelSerializer):
    product_id = serializers.UUIDField()

    class Meta:
        model = Cartitems
        fields = ['id','product_id','quantity']

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        if Cartitems.objects.filter(cart_id=cart_id,product_id=product_id).exists():

            try:
                cart_item = Cartitems.objects.get(cart_id=cart_id,product_id=product_id)
                cart_item.quantity += quantity
                cart_item.save()
                self.instance = cart_item
                return self.instance
            
            except Exception as e:
                raise serializers.ValidationError({'error':e})
            
        else: 
            try:
               
               self.instance = Cartitems.objects.create(cart_id=cart_id,**self.validated_data)   
               return self.instance
            
            except Exception as e:
                raise serializers.ValidationError({'error':e})

class UpdateCartitemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cartitems
        fields = ['quantity']


   
    
class CartSerializer(serializers.ModelSerializer):
    cart_id = serializers.UUIDField(read_only=True)
    items = CartitemsSerializer(many=True,read_only = True)
    # cart_total = serializers.SerializerMethodField(method_name='main_total')
    class Meta:
        model = Cart
        fields = ['cart_id','items','cart_total']

class OrderItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
   
    class Meta:
        model=OrderItem
        fields = ['id','product','quantity']   


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model=Order
        fields = ['id','placed_at','pending_status','owner','items']        

class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField() 

    def save(self, **kwargs):
        print(self.cart_id)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','name','bio','picture']


    # def main_total(self, cart:Cart):
    #     items = cart.items.all()
    #     return sum([item.quantity * item.product.price for item in items])    

