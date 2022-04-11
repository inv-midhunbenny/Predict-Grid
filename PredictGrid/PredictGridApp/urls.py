from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from PredictGridApp.views import Result

urlpatterns = [
    path("ipl", Result.as_view(), name="ipl_result")
]