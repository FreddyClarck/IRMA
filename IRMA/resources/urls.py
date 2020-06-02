from django.conf.urls import url
from resources import views


urlpatterns = [
    url(r'^resources/', views.resources, name='resources'),
]
