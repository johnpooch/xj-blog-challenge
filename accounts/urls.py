from django.urls import path
from .views import login, register, profile, logout

urlpatterns = [
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('logout', logout, name="logout"),
    path('profile', profile, name="profile"),
]