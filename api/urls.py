from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("products",views.ProductsViewSet)
router.register("categories",views.CategoriesViewSet)
router.register("carts", views.CartViewSet)

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews',views.ReviewViewSet, basename='product-reviews')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('cartitems',views.CartitemViewSet, basename='cart-cartitems')

# urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)),
    path('',include(product_router.urls)),
    path('',include(cart_router.urls)),

]