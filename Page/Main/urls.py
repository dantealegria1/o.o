from django import urls
from . import views

urlpatterns = [
    urls.path('home/post', views.post_list, name='post_list'),
    urls.path('home/post/<int:pk>/', views.post_detail, name='post_detail'),
    urls.path('home/post/new/', views.post_new, name='post_new'),
]