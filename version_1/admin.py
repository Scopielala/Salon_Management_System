from django.contrib import admin
from . models import Customer, Visit

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "created_at")
    search_fields = ("name", "phone")
    ordering = ("name",)

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ("customer", "services", "amount_paid", "visit_date")
    list_filter = ("visit_date",)
    search_fields = ("customer__name", "customer__phone")
    ordering = ("-visit_date",)