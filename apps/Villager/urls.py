from django.urls import path
from apps.Villager import views

urlpatterns = [
    path('create/', views.villager_create, name='villager_create'),
    path('search/', views.villager_search, name='villager_search'),
    path('profile/<str:reg_no>', views.villager_profile, name='villager_profile')
]
