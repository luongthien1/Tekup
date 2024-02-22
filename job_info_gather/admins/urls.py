
from django.urls import path
from admins.views import AdminApp

urlpatterns = [
    path("", AdminApp.index, name="index"),
    path("/crawl", AdminApp.api_crawl, name="crawl")
]
