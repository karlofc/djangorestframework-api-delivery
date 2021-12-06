from django.urls import path
from . import views

urlpatterns = [
    path('', views.HelloAuthView.as_view(), name='hello_auth'),
    path('singup/', views.UserCreateView.as_view(), name='sing_up')
]