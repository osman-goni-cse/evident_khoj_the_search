from django.contrib import admin
from django.urls import path
from registration.views import user_signup, user_login, user_logout

app_name = "registration"

urlpatterns = [
    path('register/', user_signup, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]