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

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs ={
            'password':{'required':True}
        }

    def validate(self,attrs):
        email = attrs.get('email','').strip().lower()
        username = attrs.get('username','')
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError('User with this email is already exists.')
        elif User.objects.filter(username = username).exists():
            raise serializers.ValidationError('User with this username is already exists.')
        return attrs