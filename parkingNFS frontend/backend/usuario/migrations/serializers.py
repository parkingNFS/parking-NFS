from rest_framework import serializers
from .models import Facturacion


class FacturacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facturacion
        fields = '__all__' 