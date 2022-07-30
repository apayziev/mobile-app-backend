from rest_framework import serializers
from post.models import Post, Commments

class PostSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField()
    rate_avg = serializers.FloatField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'comments_count', 'rate_avg')

class CommmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commments
        fields = '__all__'