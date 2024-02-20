from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Posts, Trend
import re


@receiver(post_save, sender=Posts)
def create_trends_instance(sender, instance, created, **kwargs):
    hashtags = re.findall(r'#\S+', instance.body)
    
    if hashtags:
        for hash in hashtags:
            print(hash[1:])
            if not Trend.objects.filter(hashtag=hash[1:]).exists():
                Trend.objects.create(hashtag=hash[1:], occurences=1)
            ## elif Trend.objects.get(hashtag=hash[1:]) != hash[1:]:
            else:
                trend = Trend.objects.get(hashtag=hash[1:])
                trend.occurences = trend.occurences + 1
                trend.save()
