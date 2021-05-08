from django.contrib import admin
from .financemodels import *
from .salesmodels import *
from .models import *
from .shipmentmodels import *
from .usermodels import *
from .inventorymodels import *
from .notamodels import *
from .cabangmodels import *
from pos.modeladmin import ShowIdAdmin

# Register your models here.
admin.site.register(Product, ShowIdAdmin)
admin.site.register(Promotion)
admin.site.register(MainCategory)
admin.site.register(SubCategoryOne)
admin.site.register(SubCategoryTwo)
admin.site.register(Supplier, ShowIdAdmin)
admin.site.register(ProductFaktur)
admin.site.register(Faktur)

# shipment
admin.site.register(Order)
admin.site.register(OrderRequest)
admin.site.register(Shipment)
admin.site.register(OrderSent)
admin.site.register(OrderReturn)
admin.site.register(ProductOrder)

# finance
admin.site.register(Spending)
admin.site.register(Payment, ShowIdAdmin)
admin.site.register(SalesTransaction, ShowIdAdmin)
admin.site.register(ProductSalesTransaction, ShowIdAdmin)

# user
admin.site.register(Employee, ShowIdAdmin)

# inventory
admin.site.register(Inventory)
admin.site.register(ProductInventory)
admin.site.register(PusatProductInventory)

# cabang
admin.site.register(Cabang, ShowIdAdmin)

# nota
admin.site.register(NotaCabang)



