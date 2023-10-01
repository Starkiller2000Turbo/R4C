from django.urls import path

from api.v1.views import download_statistic

urlpatterns = [
    path('download_statistic/', download_statistic, name='download_statistic'),
]
