from rest_framework import serializers
from .models import Standard, User


class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
