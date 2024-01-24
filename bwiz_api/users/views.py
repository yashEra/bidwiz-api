from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StandardSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

def post(request, *args, **kwargs):
    print(request.data)
    serializer = StandardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"data": serializer.data})
    else:
        return Response({'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class StandardAPIViews(APIView):
    pass



