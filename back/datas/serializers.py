from rest_framework import serializers
from .models import DepositProducts, DepositOptions

class DepositOptionsSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(read_only=True) # 외래키 필드는 읽기 전용
    class Meta:
        model = DepositOptions
        fields = '__all__'

class DepositProductsSerializer(serializers.ModelSerializer):
    options = DepositOptionsSerializer(many=True, read_only=True)
    is_liked  = serializers.SerializerMethodField()
    class Meta:
        model = DepositProducts
        fields = '__all__'

    def get_is_liked(self, obj):
        request = self.context.get('request', None)
        # user = self.context['request'].user
        user    = getattr(request, 'user', None)
        if not user or not user.is_authenticated:
            return False
        return obj.likes.filter(pk=user.pk).exists()



class DepositResultSerializer(serializers.ModelSerializer):
    # 연결된 DepositProducts 정보도 함께 보여주고 싶다면 중첩시켜도 되고,
    # 아니면 product_id만 받고 프론트에서 추가 API 호출해도 됩니다.
    product_name = serializers.CharField(source='product.fin_prdt_nm')
    kor_co_nm = serializers.CharField(source='product.kor_co_nm')
    join_way = serializers.CharField(source='product.join_way')
    spcl_cnd = serializers.CharField(source='product.spcl_cnd')
    etc_note = serializers.CharField(source='product.etc_note')
    class Meta:
        model = DepositOptions
        fields = [
            'id', 'intr_rate_type_nm', 'intr_rate', 'intr_rate2',
            'save_trm', 'product_name', 'kor_co_nm', 'join_way',
            'spcl_cnd', 'etc_note',
        ]

# 하위 금리 정보를 위한 Serializer
class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = ['id', 'intr_rate_type_nm', 'intr_rate', 'intr_rate2', 'save_trm']


# 상위 상품 정보를 위한 Serializer + 금리 포함
class DepositProductsListSerializer(serializers.ModelSerializer):
    options = DepositOptionSerializer(many=True, read_only=True)

    class Meta:
        model = DepositProducts
        fields = [
            'id',
            'kor_co_nm',
            'fin_prdt_nm',
            'etc_note',
            'join_member',
            'join_way',
            'spcl_cnd',
            'options',  # ← 여기 금리 목록 포함됨
        ]