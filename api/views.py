import uuid
from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from storeapp.models import Product,Category
from .serializers import CategorySerializer,ProductSerializer
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.exceptions import ValidationError

# Create your views here.

class MyError(APIException):
    """Readers error class"""
    def __init__(self, msg):
        APIException.__init__(self, msg)
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.message = msg


@api_view(['GET'])
def api_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def api_product(request,pk):

        try:
            product = get_object_or_404(Product,id=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Exception as e:
            raise ValidationError("Invalid UUID format: {}".format(str(e)))

        
       


@api_view(['GET'])
def api_category(request):
    categorys = Category.objects.all()
    serializer = CategorySerializer(categorys, many=True)
    return Response(serializer.data, status=200)