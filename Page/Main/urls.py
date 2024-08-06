from django import urls
from . import views

urlpatterns = [
    urls.path('home/post', views.post_list, name='post_list'),
    urls.path('home/post/<int:post_id>/', views.post_detail, name='post_detail'),
    urls.path('home/post/new/', views.post_new, name='post_new'),
    urls.path('home/post/<int:post_id>/like/', views.like_post, name='like_post'),
    urls.path('home/post/<int:post_id>/dislike/', views.dislike_post, name='dislike_post'),
]