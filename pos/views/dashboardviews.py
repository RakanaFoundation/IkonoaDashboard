from django.db.models.base import Model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from pos.forms import LoginForm
from django.views.generic import ListView
from pos.models.buyermodel import Buyer
from pos.models.cabangmodels import Cabang
from pos.models.models import *
from pos.models.financemodels import *
from django_genericfilters.views import FilteredListView
from django.contrib.auth.models import User
from demoproject.filter.forms import UserListForm
from pos.models.inventorymodels import ProductInventory


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


class TransactionList(ListView):
    model = SalesTransaction
    ordering = ['-id']
    paginate_by = 10


class UserListView(FilteredListView):
    # Normal ListView options
    template_name = 'user/user_list.html'
    paginate_by = 10
    context_object_name = 'users'
    model = User

    # FilteredListView options
    form_class = UserListForm
    search_fields = ['first_name', 'last_name', 'username', 'email']
    filter_fields = ['is_active', 'is_staff', 'is_superuser']
    default_order = 'last_name'


user_list_view = UserListView.as_view()


class InventoryList(ListView):
    model = ProductInventory
    ordering = ['-id']
    paginate_by = 10
