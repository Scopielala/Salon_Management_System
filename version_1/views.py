from urllib.parse import urlencode

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Customer, Visit
from .forms import CustomerForm, VisitForm
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, "version_1/homepage.html")

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
    success = False
    if request.method == "POST":
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = VisitForm()
    else:
        initial = {}
        phone = request.GET.get("phone")
        if phone:
            initial["phone_number"] = phone
        form = VisitForm(initial=initial)

    return render(request, "version_1/visit_form.html", {"form": form, "success": success})

def visit_list(request):
    visits = Visit.objects.select_related("customer")
    return render(request, "version_1/visit_list.html", {"visits": visits})

@login_required
def customer_profile(request, pk):
    customer = Customer.objects.get(pk=pk)
    visits = customer.visits.all()
    return render(request, "version_1/customer_profile.html", {"customer": customer, "visits": visits})
        


