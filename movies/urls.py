from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from movies import views

urlpatterns = [
    path('', views.index, name="index"),
    path('top10', views.top10, name="top10"),
]
