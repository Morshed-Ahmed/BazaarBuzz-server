from rest_framework import viewsets,filters
from .models import TopCategory, SubCategory
from .serializers import TopCategorySerializer, SubCategorySerializer

class TopCategoryListCreate(viewsets.ModelViewSet):
    queryset = TopCategory.objects.all()
    serializer_class = TopCategorySerializer


class SubCategoryListCreate(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['top_category__id']
  
