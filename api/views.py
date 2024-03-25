from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from storeapp.models import Product,Category

# Create your views here.

@api_view(['GET'])
def api_products(request):
    products = Product.objects.all()
    
    return Response({"message": "Hello, world!"})