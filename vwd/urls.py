from django.urls import path
from .import views

app_name = "vwd"
urlpatterns = [
    path('', views.vWd, name="vWd"),
    path('<str:slug>/', views.vWd_more, name="vWd_slug"),
]
