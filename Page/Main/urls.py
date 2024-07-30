from django import urls
from . import views

urlpatterns = [
    urls.path('home/', views.home, name='home'),
]