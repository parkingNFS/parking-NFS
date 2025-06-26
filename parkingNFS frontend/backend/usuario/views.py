from rest_framework import viewsets
from .models import *

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *

class FacturacionViewset(viewsets.ModelViewSet):

    queryset = Facturacion.objects.all()
    serializer_class = FacturacionSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'