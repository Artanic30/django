from django.urls import path

from . import views

app_name = 'gsurvey'
urlpatterns = [
    path('', views.ListView.as_view(), name='index'),
]
