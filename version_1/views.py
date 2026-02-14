from urllib.parse import urlencode

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Customer, Visit
from .forms import CustomerForm, VisitForm

# Create your views here.
def create_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect(f"{reverse('create_visit')}?{urlencode({'phone': customer.phone})}")
    else:
        form = CustomerForm()

    return render(request, "version_1/customer_form.html", {"form": form})

def create_visit(request):
    if request.method == "POST":
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("visit_list")
    else:
        initial = {}
        phone = request.GET.get("phone")
        if phone:
            initial["phone_number"] = phone
        form = VisitForm(initial=initial)

    return render(request, "version_1/visit_form.html", {"form": form})

def visit_list(request):
    visits = Visit.objects.select_related("customer")
    return render(request, "version_1/visit_list.html", {"visits": visits})

def customer_profile(request, pk):
    customer = Customer.objects.get(pk=pk)
    visits = customer.visits.all()
    return render(request, "version_1/customer_profile.html", {"customer": customer, "visits": visits})
        


