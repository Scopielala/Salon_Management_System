from django.shortcuts import render, redirect
from .models import Visit
from .forms import CustomerForm, VisitForm

# Create your views here.
def create_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("visit_list")
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
        form = VisitForm()

    return render(request, "version_1/visit_form.html", {"form": form})

def visit_list(request):
    visits = Visit.objects.select_related("customer")
    return render(request, "version_1/visit_list.html", {"visits": visits})
        


