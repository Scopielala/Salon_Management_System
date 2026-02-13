from django import forms
from .models import Customer, Visit

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "phone", "email"]

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ["customer", "services", "amount_paid", "visit_date", "notes"]