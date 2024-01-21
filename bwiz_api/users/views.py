from django.shortcuts import render
from rest_framework.views import APIView
from .serailizers import StandardSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class StandardAPIViews(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = StandardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        else:
            return Response({'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



