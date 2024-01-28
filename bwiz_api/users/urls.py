from django.urls import path
from . import views

urlpatterns = [
    # path('create-standard/', views.post),
    path('create-user/', views.CreateUserAPI.as_view()),
    path('update-user/<str:pk>', views.UpdateUserAPI.as_view()),
    path('login/', views.LoginAPIView.as_view()),

]
#crate urls