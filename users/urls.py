from django.urls import path
from .views import *


urlpatterns = [
    path('home/', Home.as_view()),
    path("register/", RegisterUser.as_view()),
    path("login/", LoginUser.as_view()),
    path('get-users/', GetUsersData.as_view())
]