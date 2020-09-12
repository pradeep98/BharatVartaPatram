from django.contrib import admin
from django.urls import path, include
from .views import PostList, PostDetail, PostEdit, PostCreate

urlpatterns = [
    path('posts/', PostList.as_view(), name='api-posts'),
    path('post/<int:pk>/', PostDetail.as_view(), name='api-post-detail'),
    path('post-edit/<int:pk>/', PostEdit.as_view(), name='api-post-edit'),
    path('post-create/', PostCreate.as_view(), name='api-post-create'),

]