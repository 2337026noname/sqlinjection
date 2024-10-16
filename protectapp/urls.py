
from django.urls import path
from . import views


# urlpatterns = [
# path('', views.py5test.as_view()),
# ]

urlpatterns = [
    path('', views.safe_search, name='safe_search'),
]