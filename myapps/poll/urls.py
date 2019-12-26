from django.urls import path
from . import views


app_name = 'poll'

urlpatterns = [
    path('', views.home, name='home'),
]
