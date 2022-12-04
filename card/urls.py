from django.urls import path
from . import views

urlpatterns = [

    path('', views.init),
    path('about/', views.about),
    path('card/', views.card)
]