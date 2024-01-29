from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import StandardSerializer, UserSerializer, CreateUserSerializer, UpdateUserSerializer, \
    LoginSerializer, ItemSerializer
from rest_framework.response import Response
from .models import Standard, User, Items
from knox import views as knox_views
from django.contrib.auth import login


# # Create your views here.
# @api_view(['POST'])
# def post(request, *args, **kwargs):
#     print(request.data)
#     serializer = StandardSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"data": serializer.data})
#     else:
#         return Response({'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def user(request, *args, **kwargs):
#     print(request.data)
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         d = User.objects.all().values()
#         return Response({"data": serializer.data})
#     else:
#         return Response({'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def userlogin(request, *args, **kwargs):
#     print(request.data)
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         d = User.objects.all().values()
#         return Response({"data": serializer.data})
#     else:
#         return Response({'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def userlogin(request, *args, **kwargs):
#     print(request.data)
#     d = User.objects.all().values()
#     return Response({"data": d})
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         d = User.objects.all().values()
#         return Response({"data": serializer.data})
#         # return Response({"data": serializer.data})
#     else:
#         return Response({'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def signup(request, *args, **kwargs):
#     print(request.data)

#     # Validate user input using UserSerializer
#     serializer = UserSerializer(data=request.data)

#     if serializer.is_valid():
#         # Check for unique username or email, you may customize this based on your model

#         # email = serializer.validated_data.get('email')
#         #
#         # if User.objects.filter(email=email).exists():
#         #     return Response({'error': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)

#         # Save the user if validation passes
#         serializer.save()

#         # Return a success response
#         return Response({"data": serializer.data})
#     else:
#         # Return validation errors
#         return Response({'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#         # return Response({'error': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)

class CreateUserAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class UpdateUserAPI(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer


class LoginAPIView(knox_views.LoginView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            response = super().post(request, format=None)

        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response(response.data, status=status.HTTP_200_OK)


# class ItemsAPIView(CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = ItemSerializer
#     queryset = Items.objects.all()

class ItemsAPIView(ListAPIView, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    permission_classes = (AllowAny,)
    serializer_class = ItemSerializer
    queryset = Items.objects.all()


class ElectronicsItemsAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ItemSerializer
    queryset = Items.objects.filter(category='Electronics')


class ArtsItemsAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ItemSerializer
    queryset = Items.objects.filter(category='Art')


class FasionsItemsAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ItemSerializer
    queryset = Items.objects.filter(category='Fashion')
