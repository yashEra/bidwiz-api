from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
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


class ItemDetailView(APIView):
    def get(self, request, item_id):
        try:
            item = Items.objects.get(item_id=item_id)
        except Items.DoesNotExist:
            return Response({"details": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item)  # Replace with your actual serializer
        return Response(serializer.data, status=status.HTTP_200_OK)


# Add this decorator to allow cross-origin requests for development purposes
# def handle_bid_submission(request, item_id):
# @csrf_protect
@csrf_exempt
@api_view(['POST'])
def handle_bid_submission(request, item_id):
    try:
        # Retrieve the bid amount from the request's POST data
        # bid_amount_str = request.data.get('current_max_bid')

        # Check if the bid amount is not empty
        if item_id is not None and item_id.strip():
            bid_amount = float(item_id)

            # Assuming you have a model named 'Item' with a field 'current_bid_price'
            item = Items.objects.get(item_id=item_id)
            # Update the current_bid_price field
            # item.current_max_bid = bid_amount
            # item.save()
            serializer = ItemSerializer(
                item,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            # You can also perform additional logic here if needed

            # Respond with a success message
            return JsonResponse({'message': 'Bid updated successfully'})
        else:
            # If bid amount is empty or None, respond with an error message
            return JsonResponse({'error': 'Bid amount is missing or invalid'}, status=400)

    except Exception as e:
        # Handle any errors that might occur
        return JsonResponse({'error': str(e)}, status=500)


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})
