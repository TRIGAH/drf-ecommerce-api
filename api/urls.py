from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("products",views.ProductsViewSet)
router.register("categories",views.CategoriesViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('',include(router.urls)),

# ]