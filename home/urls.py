from django.urls import path,include
from .import views

app_name = "home"
urlpatterns = [
    path('', views.index, name="index"),
    path('women-bleeders/', views.womenBleeders, name='womenBleeders'),
    path('treatments/', views.treatments, name='treatment'),
    path('inhibitors/', views.inhibitors, name='inhibitors'),
    path('treatments-details/<str:slug>/<str:category>/', views.treatmentsDetails, name='treatments_slug'),
    path('contact-us',views.contactUs, name="contactUs"),
    path('real-stories/<int:pk>/',views.realstories, name="realStories"),
]
