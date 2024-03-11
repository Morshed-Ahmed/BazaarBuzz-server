from django.urls import path,include
from .views import ProductListCreate,ProductReviewViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('products', ProductListCreate) 
router.register('products-review', ProductReviewViewSet) 


urlpatterns = [
    path('', include(router.urls)),
]
