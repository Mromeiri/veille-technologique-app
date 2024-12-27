from django.urls import path

from django.contrib.auth import views as auth_views

from veille_app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
