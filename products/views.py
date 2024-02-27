from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets,filters


class TopSubCategoryFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        top_category = request.query_params.get('top_category')
        sub_category = request.query_params.get('sub_category')
        search_query = request.query_params.get('search')

        if top_category:
            queryset = queryset.filter(top_category__name=top_category)
        if sub_category:
            queryset = queryset.filter(sub_category__name=sub_category)
        
        if search_query == "All":
            return queryset
        
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        return queryset
        
class ProductListCreate(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter,TopSubCategoryFilterBackend]
    search_fields = ['name']