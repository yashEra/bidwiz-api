from django.urls import path
from . import views

urlpatterns = [
    path('create-standard/', views.post),
    path('create-user/', views.user),
    path('login-user/', views.userlogin),

]
#crate urls