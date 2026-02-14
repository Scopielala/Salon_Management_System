from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("dashboard/", views.visit_list, name="dashboard"),
    path("customers/new/", views.create_customer, name="create_customer"),
    path("visits/new/", views.create_visit, name="create_visit"),
    path("customers/<int:pk>/", views.customer_profile, name="customer_profile"),
]