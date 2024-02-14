from django.forms import ModelForm
from .models import Posts, PostAttachment


class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ('body',)


class AttachmentForm(ModelForm):
    class Meta:
        model = PostAttachment
        fields = ('image',)