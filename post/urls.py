from django.urls import path
from post.views import CommentList

urlpatterns = [
    path('', CommentList.as_view(), name='post-list')
]