from django.urls import path
from . import views

urlpatterns = [
    path('create-standard/', views.StandardAPIViews.as_view()),
]
