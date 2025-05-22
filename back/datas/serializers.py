from rest_framework import serializers
from .models import DepositProducts, DepositOptions

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'


class DepositOptionsSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(read_only=True) # 외래키 필드는 읽기 전용
    class Meta:
        model = DepositOptions
        fields = '__all__'