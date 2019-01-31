# accounts/urls.py
from django.urls import path

from accounts import views as accounts_views


urlpatterns = [
    path('signup/', accounts_views.SignUp, name='signup'),
]