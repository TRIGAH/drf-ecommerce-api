import uuid
from storeapp.models import Product,Category,Review,Cart,Cartitems,Profile
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ReviewSerializer,
    CartSerializer,
    CartitemsSerializer,
    AddCartitemsSerializer,
    UpdateCartitemsSerializer,
    ProfileSerializer
    )
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination 
from django_filters.rest_framework import DjangoFilterBackend
from api.filter import ProductFilter
# Create your views here.

class ProductsViewSet(ModelViewSet):
    queryset  = Product.objects.all()
    serializer_class = ProductSerializer  
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['old_price']
    pagination_class = PageNumberPagination

            
class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 
      
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer 

    def get_queryset(self):
        queryset = Review.objects.filter(product_id = self.kwargs['product_pk'])
        return queryset

    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}
      

class CartViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartitemViewSet(ModelViewSet):

    http_method_names = ['get','post','patch','delete']

    def get_queryset(self):
        queryset = Cartitems.objects.filter(cart_id = self.kwargs['cart_pk'])
        return queryset
    
    def get_serializer_class(self):
        
        if self.request.method == 'POST':
            return AddCartitemsSerializer
        
        elif self.request.method == 'PATCH':
            return UpdateCartitemsSerializer
        
        return CartitemsSerializer
    
    def get_serializer_context(self):
        return {'cart_id':self.kwargs['cart_pk']}
    


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = (MultiPartParser,FormParser)