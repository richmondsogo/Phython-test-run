from django.urls import path
from . import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('authorizer', views.AuthorizedView.as_view(), name='authorizer'),
]
