from django.db import models
import uuid
from accounts.models import User
from django.utils.timesince import timesince

# Create your models here.

class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_attachments')

    owner = models.ForeignKey(User, related_name='posts_attachments', on_delete=models.CASCADE)

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:5173' + self.image.url
        else:
            return ''


class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
    
    def created_since(self):
       return timesince(self.created_at)


class Posts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    attachments = models.ManyToManyField(PostAttachment, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    likes = models.ManyToManyField(Like, blank=True)
    likes_count = models.IntegerField(default=0)

    comments = models.ManyToManyField(Comment, blank=True)
    comments_count = models.IntegerField(default=0)

    class Meta:
        ordering = ('-created_at',)

    def created_since(self):
        return timesince(self.created_at)

class Trend(models.Model):
    hashtag = models.CharField(max_length=255)
    occurences = models.IntegerField()
