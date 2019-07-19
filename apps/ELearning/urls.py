from django.urls import path
from apps.ELearning import views

urlpatterns = [
    path('list', views.tutorial_list, name='tutorial_list')
]