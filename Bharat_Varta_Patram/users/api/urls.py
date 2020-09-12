from django.contrib import admin
from django.urls import path, include
from .views import UserRegistrationApi
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', UserRegistrationApi.as_view(), name='api-user-registration'),
    path('login/', obtain_auth_token, name='api-login'),
]