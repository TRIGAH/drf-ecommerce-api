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
         
            
            


@api_view(['GET','POST'])
def api_categorys(request):

    if request.method == 'GET':
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
       serializer = CategorySerializer(data=request.data)
       serializer.is_valid(raise_exception = True)
       serializer.save()
       return Response(serializer.data)


@api_view(['GET','PUT','DELETE'])
def api_category(request,pk):

        try:
            category = get_object_or_404(Category,category_id=pk)

            if request.method == 'GET':
                serializer = CategorySerializer(category)
                return Response(serializer.data)
            
            if request.method == 'PUT':
               serializer = CategorySerializer(category,data=request.data) 
               serializer.is_valid(raise_exception = True) 
               serializer.save()
               return Response(serializer.data)
            
            if request.method == 'DELETE':
                category.delete()
                return Response(status = status.HTTP_204_NO_CONTENT)

        except Exception as e:
            raise ValidationError("Invalid UUID format: {}".format(str(e)))