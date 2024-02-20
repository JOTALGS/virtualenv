from django.urls import path
from . import api

urlpatterns = [
    path('', api.post_list, name='posts_list'),
    path('<uuid:pk>/', api.post_detail, name='post_detail'),
    path('<uuid:pk>/like/', api.post_like, name='post_like'),
    path('<uuid:pk>/comment/', api.post_create_comment, name='post_create_comment'),
    path('profile/<uuid:id>/', api.post_list_profile, name='post_list_profile'),
    path('create/', api.create_post, name='create_post'),
    path('top/trends/', api.get_top_trends, name='top_trends'),
    path('trends/<str:input>/', api.get_search_trends, name='search_trends'),
]