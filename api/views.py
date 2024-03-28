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


@api_view(['GET','POST'])
def api_products(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=200)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

         


@api_view(['GET','PUT'])
def api_product(request,pk):
        if request.method == 'GET':
            try:
                product = get_object_or_404(Product,id=pk)
                serializer = ProductSerializer(product)
                return Response(serializer.data)
            except Exception as e:
                raise ValidationError("Invalid UUID format: {}".format(str(e)))
            
            


@api_view(['GET'])
def api_categorys(request):
    categorys = Category.objects.all()
    serializer = CategorySerializer(categorys, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def api_category(request,pk):

        try:
            category = get_object_or_404(Category,category_id=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Exception as e:
            raise ValidationError("Invalid UUID format: {}".format(str(e)))