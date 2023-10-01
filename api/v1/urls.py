from django.urls import path

from api.v1.views import create_robot

urlpatterns = [
    path('', create_robot, name='new_robot'),
]
