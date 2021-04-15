from django.db.models.signals import post_save
from django.dispatch import receiver
from pos.models import ProductFaktur
from pos.inventorymodels import Inventory, ProductInventory, PusatProductInventory
from pos.salesmodels import ProductSalesTransaction
from django.db.models import F

@receiver(post_save, sender=ProductFaktur, dispatch_uid="add_pusat_inventory")
def updatePusatInventory(sender, instance, **kwargs):
    try:
        pusatProductInventory = PusatProductInventory.objects.get(product=instance.product)    
        PusatProductInventory.objects.filter(product=pusatProductInventory.product).update(stock=F('stock') + instance.quantity) 
    except PusatProductInventory.DoesNotExist:
        PusatProductInventory.objects.create(
            product = instance.product,
            stock = instance.quantity
        )


def increaseCabangCreateFunc(productSalesTransaction, inventory):
    ProductInventory.objects.create(
            inventory = inventory,
            product = productSalesTransaction.product,
            stock = productSalesTransaction.quantity
        )

def reduceCabangCreateFunc(productSalesTransaction, inventory):
    ProductInventory.objects.create(
            inventory = inventory,
            product = productSalesTransaction.product,
            stock = 0
        )

def reduceStockFunction(productInventory, productSalesTransaction):
    ProductInventory.objects.filter(product=productInventory.product).update(stock=F('stock') - productSalesTransaction.quantity) 

def incrementStockFunction(productInventory, productSalesTransaction):
    ProductInventory.objects.filter(product=productInventory.product).update(stock=F('stock') + productSalesTransaction.quantity) 

@receiver(post_save, sender=ProductSalesTransaction, dispatch_uid="reduce_cabang_inventory")
def reduce_cabang_inventory(sender, instance, **kwargs):
    updateCabangInventory(instance, reduceStockFunction, reduceCabangCreateFunc)

def increment_cabang_inventory(productSalesTransaction):
    updateCabangInventory(productSalesTransaction, incrementStockFunction, incrementStockFunction)

def updateCabangInventory(instance, updateStockFunction, createProductInventoryFunc):
    cabang = instance.salesTransaction.cabang
    try:
        inventory = Inventory.objects.get(cabang=cabang)
    except Inventory.DoesNotExist:
        inventory = Inventory.objects.create(
            cabang = cabang
        )

    try:
        productInventory = ProductInventory.objects.get(product=instance.product, inventory=inventory)    
        updateStockFunction(productInventory, instance)
    except ProductInventory.DoesNotExist:
        createProductInventoryFunc(instance, inventory)

    
