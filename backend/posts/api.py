from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer, TrendSerializer
from .models import Posts, Like, Comment, Trend
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import PostForm, AttachmentForm
from accounts.models import User
from accounts.serializers import UserSerializer


# Create your views here.

@api_view(['GET'])
def post_list(request):
    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)

    posts = Posts.objects.filter(owner_id__in=list(user_ids))

    trend = request.GET.get('trend', '')

    if trend:
        posts = posts.filter(body__icontains='#' + trend)

    serializer = PostSerializer(posts, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def post_detail(request, pk):
    post = Posts.objects.get(pk=pk)

    return JsonResponse({
        'post': PostDetailSerializer(post).data
    })


@api_view(['GET'])
def post_list_profile(request, id):
    user = User.objects.get(pk=id)
    posts = Posts.objects.filter(owner_id=id)

    posts_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)

    return JsonResponse({
        'posts': posts_serializer.data,
        'user': user_serializer.data
    }, safe=False)

@api_view(['POST'])
def create_post(request):
    form = PostForm(request.data)
    attachment = None
    attachment_form = AttachmentForm(request.POST, request.FILES)

    print('att', request.FILES)
    if attachment_form.is_valid():
        attachment = attachment_form.save(commit=False)
        attachment.owner = request.user
        attachment.save()

    if form.is_valid():
        post = form.save(commit=False)
        post.owner = request.user
        post.save()

        if attachment:
            post.attachments.add(attachment)

        user = request.user
        user.posts_count = user.posts_count + 1
        user.save()

        serializer = PostSerializer(post)

        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'add somehting here later!...'})
    

@api_view(['POST'])
def post_like(request, pk):
    post = Posts.objects.get(pk=pk)

    if not post.likes.filter(owner=request.user):
        like = Like.objects.create(owner=request.user)

        post = Posts.objects.get(pk=pk)
        post.likes_count = post.likes_count + 1
        post.likes.add(like)
        post.save()

        return JsonResponse({'message': 'like created'})
    else:
        return JsonResponse({'message': 'post already liked'})


@api_view(['POST'])
def post_create_comment(request, pk):
    comment = Comment.objects.create(body=request.data.get('body'), owner=request.user)

    post = Posts.objects.get(pk=pk)
    post.comments.add(comment)
    post.comments_count = post.comments_count + 1
    post.save()

    serializer = CommentSerializer(comment)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def get_trends(request):
    serializer = TrendSerializer(Trend.objects.all(), many=True)

    return JsonResponse(serializer.data, safe=False)