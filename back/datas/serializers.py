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


class DepositResultSerializer(serializers.ModelSerializer):
    # 연결된 DepositProducts 정보도 함께 보여주고 싶다면 중첩시켜도 되고,
    # 아니면 product_id만 받고 프론트에서 추가 API 호출해도 됩니다.
    product_name = serializers.CharField(source='product.fin_prdt_nm')
    class Meta:
        model = DepositOptions
        fields = [
          'id', 'intr_rate_type_nm', 'intr_rate', 'intr_rate2',
          'save_trm', 'product_name',
        ]

