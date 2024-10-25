from django.urls import path
from . import views
urlpatterns = [
    path('', views.myapp_search, name='myapp_search'),
]