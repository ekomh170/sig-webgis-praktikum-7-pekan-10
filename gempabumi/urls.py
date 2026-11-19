from django.urls import path
from . import views

urlpatterns = [
    path('', views.gempaterkini, name='gempaterkini'),
    path('api/', views.api_gempaterkini, name='api_gempaterkini'),
]
