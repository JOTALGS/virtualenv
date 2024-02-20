# -*- coding: utf-8 -*-

import django
import os
import sys

from datetime import timedelta
from collections import Counter
from django.utils import timezone


sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wey_backend.settings")
django.setup()


from accounts.models import User


users = User.objects.all()

for user in users:
    # Clear the suggestion list
    user.collab_suggestions.clear()

    print('Find friends for:', user)

    for friend in user.friends.all():
        print('Is friend with:', friend)

        for friendsfriend in friend.friends.all():
            if friendsfriend not in user.friends.all() and friendsfriend != user:
                user.collab_suggestions.add(friendsfriend)
    
    print()