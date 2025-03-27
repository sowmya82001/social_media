from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link post to a user
    title = models.CharField(max_length=255, default="Untitled")  # Default title added
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Image field
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return self.title
