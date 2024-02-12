from django.urls import path,include
from .views import TopCategoryListCreate, SubCategoryListCreate
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('topcategories', TopCategoryListCreate)
router.register('subcategories', SubCategoryListCreate)

urlpatterns = [
    path('', include(router.urls)),
]
