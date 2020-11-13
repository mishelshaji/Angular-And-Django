from django.urls import path
from .views import *

urlpatterns = [
    path('', MovieList.as_view()),
]