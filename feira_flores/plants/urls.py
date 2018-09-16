from django.urls import path

from feira_flores.plants import views

app_name = 'plants'
urlpatterns = [
    path('', views.index, name='index')
]
