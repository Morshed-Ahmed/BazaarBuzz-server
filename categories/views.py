from rest_framework import viewsets
from .models import TopCategory, SubCategory
from .serializers import TopCategorySerializer, SubCategorySerializer

class TopCategoryListCreate(viewsets.ModelViewSet):
    queryset = TopCategory.objects.all()
    serializer_class = TopCategorySerializer


class SubCategoryListCreate(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

