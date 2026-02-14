from django import forms
from .models import Customer, Visit

SERVICE_CHOICES = [
    ("Haircut", "Haircut"),
    ("Shave", "Shave"),
    ("Hair Wash", "Hair Wash"),
    ("Hair Color", "Hair Color"),
    ("Hair Color(Black)", "Hair Color(Black)"),
    ("DreadLock", "DreadLock"),
    ("Home Services", "Home Services"),
]


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "phone", "email"]


class VisitForm(forms.ModelForm):
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={"placeholder": "Enter customer phone number", "autocomplete": "off"}),
    )
    services = forms.MultipleChoiceField(
        choices=SERVICE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Visit
        fields = ["services", "amount_paid", "visit_date", "notes"]

    def clean_phone_number(self):
        phone = self.cleaned_data["phone_number"].strip()
        try:
            self._customer = Customer.objects.get(phone=phone)
        except Customer.DoesNotExist:
            raise forms.ValidationError("No customer registered with this phone number.")
        return phone

    def clean_services(self):
        return ", ".join(self.cleaned_data["services"])

    def save(self, commit=True):
        visit = super().save(commit=False)
        visit.customer = self._customer
        if commit:
            visit.save()
        return visit
