
from django.urls import path
from . import views


urlpatterns = [
    path('', views.protectapp_search, name='protectapp_search'),
]