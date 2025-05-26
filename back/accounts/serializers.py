from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class CustomUserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'username', 
            'password', 
            'password2', 
            'age', 
            'nationality', 
            'name',
        ]
        extra_kwargs = {
            'name': {'required': True},
            'age': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "비밀번호가 일치하지 않습니다."}
            )
        return attrs

    def create(self, validated_data):
        # password2 필드는 제거
        validated_data.pop('password2', None)
        
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            name=validated_data['name'],
            age=validated_data['age'],
            nationality=validated_data.get('nationality', '')  # 선택적 필드
        )
        return user
    


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'age', 'nationality')