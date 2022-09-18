from django.urls import path
from .import views

app_name = 'hemophilia'

urlpatterns = [
    path('', views.hemophilia, name="hemophilia"),
    path('about/<str:slug>/<str:category>/', views.about, name="about"),
]
