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

    def validate(self,pk):
        if len(pk.strip()) != 32:
            raise ValidationError("Not a valid UUID")     

    # def validate(self, data):
    #     # Perform validation check here

    #     try:
    #         # Code that might raise the badly formed hexadecimal UUID string exception
    #         uuid_value = uuid4(data['id'])
    #     except ValueError as e:
    #         # Handle the badly formed hexadecimal UUID string exception
    #         raise ValidationError("Invalid UUID format: {}".format(str(e)))
    #     except Exception as e:
    #         # Handle other exceptions
    #         raise serializers.ValidationError("An error occurred: {}".format(str(e)))
    #     return data