from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from PredictGridApp.views import Login, Logout, Result

urlpatterns = [
    path("ipl", Result.as_view(), name="ipl_result"),
    path("login",Login.as_view(), name="login"),
    path("logout",Logout.as_view(), name="logout")

]