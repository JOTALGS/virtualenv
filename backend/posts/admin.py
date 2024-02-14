from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PostAttachment, Posts, Comment, Like, Trend


# Register your models here.

admin.site.register(Posts)
admin.site.register(PostAttachment)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Trend)
