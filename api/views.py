import uuid
import requests
from storeapp.models import Product,Category,Review,Cart,Cartitems,Profile
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination 
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from api.filter import ProductFilter
# Create your views here.



def initiate_payment(amount, email, order_id):
    url = "https://api.flutterwave.com/v3/payments"
    headers = {
        "Authorization": f"Bearer {settings.FLW_SEC_KEY}"
        
    }
    
    data = {
        "tx_ref": str(uuid.uuid4()),
        "amount": str(amount), 
        "currency": "USD",
        "redirect_url": "http:/127.0.0.1:8000/api/orders/confirm_payment/?o_id=" + order_id,
        "meta": {
            "consumer_id": 23,
            "consumer_mac": "92a3-912ba-1192a"
        },
        "customer": {
            "email": email,
            "phonenumber": "080****4528",
            "name": "Yemi Desola"
        },
        "customizations": {
            "title": "Pied Piper Payments",
            "logo": "http://www.piedpiper.com/app/themes/joystick-v27/images/logo.png"
        }
    }
    

    try:
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()
        return Response(response_data)
    
    except requests.exceptions.RequestException as err:
        print("the payment didn't go through")
        return Response({"error": str(err)}, status=500)







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
    


class OrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        return OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(owner=user)
    
    def get_serializer_context(self):
        return {'user_id':self.request.user.id}



class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = (MultiPartParser,FormParser)

    def create(self,request):
        name = request.data['name']
        bio = request.data['bio']
        picture = request.data['picture']

        Profile.objects.create(name=name, bio=bio, picture=picture )

        return Response("Profile Created Successfully", status = status.HTTP_201_CREATED)