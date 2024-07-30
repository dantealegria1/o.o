from django import urls
from . import views

urlpatterns = [
    urls.path('login/', views.login, name='login'),
    urls.path('users/', views.users, name='users'),
    urls.path('signup/', views.signup, name='signup'),
    urls.path('', views.index, name='index'),
]