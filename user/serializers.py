from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'created', 'modified']

from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from core.models import Profile
from user.models import User
from user.serializers import UserSerializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, max_length=128)
    weight = serializers.FloatField(required=False)  # New field for weight

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'created', 'modified', 'weight']

    def create(self, validated_data):
        password = validated_data.pop('password')
        weight = validated_data.pop('weight', None)  # Retrieve weight if provided, default to None
        user = User.objects.create_user(password=password, **validated_data)
        
        if weight is not None:
            Profile.objects.create(user=user, weight=weight)
        
        return user



class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data['access'] = str(refresh.access_token)
        data['refresh'] = str(refresh)
        data['user'] = UserSerializer(self.user).data

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data