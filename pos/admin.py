from django.contrib import admin
from pos.models.modeladmin import ShowIdAdmin
from pos.models.salesmodels import ProductSalesTransaction
from pos.models.models import Faktur, MainCategory, Product, ProductFaktur, SubCategoryOne, SubCategoryTwo, Supplier
from pos.models.promotionmodels import Promotion
from pos.models.shipmentmodels import Order, OrderRequest, OrderReturn, OrderSent, ProductOrder, Shipment
from pos.models.usermodels import Employee
from pos.models.inventorymodels import Inventory, ProductInventory, PusatProductInventory
from pos.models.notamodels import NotaCabang
from pos.models.cabangmodels import Cabang
from pos.models.financemodels import Payment, SalesTransaction, Spending
from pos.models.districtmodels import District

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

admin.site.register(District)



