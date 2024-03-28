import uuid
from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from storeapp.models import Product,Category
from .serializers import CategorySerializer,ProductSerializer
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

# Create your views here.

class ApiProducts(APIView):

    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
         
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
               

class ApiProduct(APIView):
     
    def get(self,request,pk):
        try:
            product = get_object_or_404(Product,id=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Exception as e:
                raise ValidationError("Invalid UUID format: {}".format(str(e)))
        

    def put(self,request,pk):    
        try:
            product = get_object_or_404(Product,id=pk)
            serializer = ProductSerializer(product,data=request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
                raise ValidationError("Invalid UUID format: {}".format(str(e)))
         
    def delete(self,request,pk):
        try:
            product = get_object_or_404(Product,id=pk)
            product.delete()
        except Exception as e:
            raise ValidationError("Invalid UUID format: {}".format(str(e)))
        

class ApiCategories(APIView):

    def get(self,request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
         
    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)            
            

class ApiCategory(APIView):
     
    def get(self,request,pk):
        try:
            category = get_object_or_404(Category,category_id=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Exception as e:
                raise ValidationError("Invalid UUID format: {}".format(str(e)))
        

    def put(self,request,pk):    
        try:
            category = get_object_or_404(Category,category_id=pk)
            serializer = CategorySerializer(category,data=request.data)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
                raise ValidationError("Invalid UUID format: {}".format(str(e)))
        
    def delete(self,request,pk):
        try:
            category = get_object_or_404(Category,category_id=pk)
            category.delete()
        except Exception as e:
            raise ValidationError("Invalid UUID format: {}".format(str(e)))

