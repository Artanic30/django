from django.urls import path

from . import views

app_name = 'gsurvey'
urlpatterns = [
    path(r'user', views.Student.as_view(), name='user'),
    path(r'site', views.Sites.as_view(), name='site')
]
