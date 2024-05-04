from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'sector', 'date', 'open_price', 'high_price', 'low_price', 'close_price', 'volume']
