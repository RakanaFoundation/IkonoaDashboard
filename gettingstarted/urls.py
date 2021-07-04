import hello.views
from django.conf.urls import url
from pos.views.dashboardviews import *
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .logintokenpairview import LoginTokenPairView
admin.autodiscover()

urlpatterns = [
    url(r'^user/$', user_list_view, name='user_filter_view'),
    path("", hello.views.index, name="index"),
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('buyer/', BuyerList.as_view(), name='buyer'),
    path('supplier/', SupplierList.as_view(), name='supplier'),
    path('transaksi/', TransactionList.as_view(), name='transaksi'),
    path('gudang/', InventoryList.as_view(), name='gudang'),
    path("pos/", include("pos.urls")),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('api-token-auth/', LoginTokenPairView.as_view(), name='api-tokn-auth'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
