from django.conf.urls import url
from faculties import views


urlpatterns = [
    url(r'^faculties/', views.faculties, name='faculties'),
]
