
from rest_framework import generics
from django.db.models import Count,Sum, Avg
from post.models import Post, Commments
from post.serializers import PostSerializer, CommmentsSerializer

class CommentList(generics.ListAPIView):
    # annotate COUNT of comments adns AVG of rate
    queryset = Post.objects.annotate(comments_count=Count('comments'), 
                                    rate_avg=Avg('comments__rate'))
    serializer_class = PostSerializer
    
