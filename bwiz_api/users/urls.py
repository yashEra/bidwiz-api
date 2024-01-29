from django.urls import path
from rest_framework.generics import RetrieveAPIView

from . import views
from knox.views import LogoutView,LogoutAllView

from .views import ItemsAPIView, ElectronicsItemsAPIView, ArtsItemsAPIView, FasionsItemsAPIView, ItemDetailView, \
    get_csrf_token, handle_bid_submission

urlpatterns = [
    # path('create-standard/', views.post),
    path('create-user/', views.CreateUserAPI.as_view()),
    path('update-user/<str:pk>', views.UpdateUserAPI.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view()),
    path('items/', ItemsAPIView.as_view(), name='items-list'),
    # path('items/<str:item_id>/', ItemsAPIView.as_view(), name='item-detail'),
    path('electronics/', ElectronicsItemsAPIView.as_view(), name='electronics-items-list'),
    path('arts/', ArtsItemsAPIView.as_view(), name='arts-items-list'),
    path('fasions/', FasionsItemsAPIView.as_view(), name='fasions-items-list'),
    path('items/<int:item_id>/', ItemDetailView.as_view(), name='item-detail'),
    path('items/<str:item_id>/bid/', handle_bid_submission, name='handle_bid_submission'),
    path('csrf/', get_csrf_token, name='get_csrf_token'),

    # path('items/<int:item_id>/', views.retrieve),

]
#crate urls