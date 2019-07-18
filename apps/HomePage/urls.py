from django.urls import path
from apps.HomePage import views

urlpatterns = [
    path('', views.homepage, name='homepage')
]
