from . import views
from django.urls import path

appName = 'ElectionCode'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('live/', views.live, name='live')
]
