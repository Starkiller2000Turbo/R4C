from django.urls import path

from api.v1.views import create_robot

app_name = '%(app_label)s'


urlpatterns = [
    path('', create_robot, name='new_robot'),
]
