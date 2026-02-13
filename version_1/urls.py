from django.urls import path
from . import views

urlpatterns = [
    path("", views.visit_list, name="visit_list"),
    path("customers/new/", views.create_customer, name="create_customer"),
    path("visits/new/", views.create_visit, name="create_visit"), 
]