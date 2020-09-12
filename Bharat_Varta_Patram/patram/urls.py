from django.contrib import admin
from django.urls import path, include
from .views import postDetail, PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,PostCommentCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', postDetail, name='post-detail'),
    path('post/add/', PostCreateView.as_view(), name='post-create'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    
]