from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', view, name='api_view'),
    path('create/', create, name='api_create'),
    path('<int:id>/', view_single, name='api_view_single'),
    path('update/<int:id>/', update, name='api_update'),
    path('delete/<int:id>/', delete, name='api_delete'),
]