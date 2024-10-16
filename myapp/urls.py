
from django.urls import path
from . import views
# urlpatterns = [
# path('', views.py5test.as_view()),
# ]
urlpatterns = [
    path('', views.vulnerable_search, name='vulnerable_search'),
]