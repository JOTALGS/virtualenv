from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from accounts.models import User
from accounts.serializers import UserSerializer


@api_view(['GET'])
def autofill_users(request, input):

    users_match = User.objects.filter(name__istartswith=input.strip())
    users_serializer = UserSerializer(users_match, many=True)


    return JsonResponse({
        'matchs': users_serializer.data,
    }, safe=False)


@api_view(['GET'])
def suggest_users(request):

    users_to_suggest = User.objects.all()
    print('user suggest', users_to_suggest)
    users_serializer = UserSerializer(users_to_suggest, many=True)


    return JsonResponse({
        'suggestions': users_serializer.data,
    }, safe=False)