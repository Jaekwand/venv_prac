from django.urls import path

from payment import views

urlpatterns = [
    path("cart/", views.payment_cart),
    path("complete/", views.payment_complete),
    path("purchase/", views.payment_purchase)
]