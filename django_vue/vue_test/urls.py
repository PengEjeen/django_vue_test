from django.urls import path
from .views import PostListCreate

urlpatterns = [
    path('api/posts/', PostListCreate.as_view(), name='post-list-create'),
]
