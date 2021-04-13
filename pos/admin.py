from django.contrib import admin

from .financemodels import *
from .salesmodels import *
from .models import *
from .shipmentmodels import *
from .usermodels import *
from .inventorymodels import *
from .notamodels import *
from .cabangmodels import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Promotion)
admin.site.register(MainCategory)
admin.site.register(SubCategoryOne)
admin.site.register(SubCategoryTwo)
admin.site.register(Supplier)
admin.site.register(ProductFaktur)
admin.site.register(Faktur)

# shipment
admin.site.register(Order)
admin.site.register(OrderRequest)
admin.site.register(OrderReceived)
admin.site.register(Shipment)
admin.site.register(OrderSent)
admin.site.register(OrderReturn)

# finance
admin.site.register(Spending)
admin.site.register(Payment)
admin.site.register(SalesTransaction)
admin.site.register(ProductSalesTransaction)

# user
admin.site.register(Employee)

# inventory
admin.site.register(Inventory)
admin.site.register(ProductInventory)

# cabang
admin.site.register(Cabang)

# nota
admin.site.register(NotaCabang)



