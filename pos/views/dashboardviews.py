from django.db.models.base import Model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from pos.forms import LoginForm
from django.views.generic import ListView
from pos.models.buyermodel import Buyer
from pos.models.cabangmodels import Cabang
from pos.models.models import *


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "public/pages/login.html", {"form": form, "msg": msg})


class BuyerList(ListView):
    model = Buyer
    ordering = ['-id']
    paginate_by = 10


class CabangList(ListView):
    model = Cabang


class SupplierList(ListView):
    model = Supplier
    ordering = ['-id']
    paginate_by = 10
