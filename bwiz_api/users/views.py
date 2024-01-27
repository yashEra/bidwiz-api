from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import StandardSerializer, UserSerializer
from rest_framework.response import Response
from .models import Standard, User


# Create your views here.
@api_view(['POST'])
def post(request, *args, **kwargs):
    print(request.data)
    serializer = StandardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"data": serializer.data})
    else:
        return Response({'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user(request, *args, **kwargs):
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        d = User.objects.all().values()
        return Response({"data": serializer.data})
    else:
        return Response({'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def userlogin(request, *args, **kwargs):
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        d = User.objects.all().values()
        return Response({"data": serializer.data})
    else:
        return Response({'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def userlogin(request, *args, **kwargs):
    print(request.data)
    d = User.objects.all().values()
    return Response({"data": d})
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        d = User.objects.all().values()
        return Response({"data": serializer.data})
        # return Response({"data": serializer.data})
    else:
        return Response({'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def signup(request, *args, **kwargs):
    print(request.data)

    # Validate user input using UserSerializer
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        # Check for unique username or email, you may customize this based on your model

        # email = serializer.validated_data.get('email')
        #
        # if User.objects.filter(email=email).exists():
        #     return Response({'error': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Save the user if validation passes
        serializer.save()

        # Return a success response
        return Response({"data": serializer.data})
    else:
        # Return validation errors
        return Response({'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        # return Response({'error': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)