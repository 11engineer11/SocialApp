from django.urls import path
from .views import *

app_name='home'
urlpatterns = [
    path('connect/<operation>/<int:pk>/', change_friends, name='change_friends'),

    
]