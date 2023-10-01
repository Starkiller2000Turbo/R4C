from django.urls import include, path

app_name = '%(app_label)s'


urlpatterns = [
    path('', include('api.v1.urls')),
]
