from django.urls import path

from local import views

urlpatterns = [
    path("local-shops/", views.local_local_shops),
]