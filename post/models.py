from django.db import models
from helpers.models import BaseModel

# Create your models here.

class Post(BaseModel):
    title = models.CharField(max_length=256)
    content = models.TextField()

    def __str__(self):
        return self.title

class Commments(BaseModel):
    content = models.TextField()
    rate = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.content
   
