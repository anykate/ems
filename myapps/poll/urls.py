from django.urls import path
from . import views


app_name = 'poll'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:question_id>/question/', views.question_details, name='question_details'),
]
