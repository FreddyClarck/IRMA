from django.conf.urls import url
from divisions import views


urlpatterns = [
    url(r'^divisions/', views.divisions, name='divisions'),
]
