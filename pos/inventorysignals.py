from django.db.models.signals import post_save
from django.dispatch import receiver
from pos.models.models import ProductFaktur
from pos.models.inventorymodels import Inventory, ProductInventory, PusatProductInventory
from pos.models.salesmodels import ProductSalesTransaction
from django.db.models import F
from django.db import IntegrityError, transaction

# yang bener 
def incrementPusatInventory(product, quantity):
    try:
        pusatProductInventory = PusatProductInventory.objects.get(product=product)    
        pusatProductInventory.stock = F('stock') + quantity
        pusatProductInventory.save()
    except PusatProductInventory.DoesNotExist:
        PusatProductInventory.objects.create(
            product = product,
            stock = quantity
        )

def reducePusatInventory(product, quantity):
    pusatProductInventory = PusatProductInventory.objects.get(product=product)    
    productDesc = pusatProductInventory.product.description
    with transaction.atomic():
        try:
            pusatProductInventory.stock = F('stock') - quantity
            pusatProductInventory.save()
            pusatProductInventory = PusatProductInventory.objects.get(product=product)    
            if pusatProductInventory.stock < 0 :
                raise ValueError("Not enough stock for " + productDesc)
        except PusatProductInventory.DoesNotExist:
            PusatProductInventory.objects.create(
                product = product,
                stock = 0
            )
        except IntegrityError:
            raise ValueError("Not enough stock for " + productDesc)

def incrementCabangInventory(cabang, product, quantity):
    inventory = getOrCreateInventory(cabang)
    increaseOrCreateProductInventory(product, inventory, quantity)

def reduceCabangInventory(cabang, product, quantity):
    inventory = getOrCreateInventory(cabang)
    reduceOrCreateProductInventory(product, inventory, quantity)
    
def getOrCreateInventory(cabang):
    try:
        inventory = Inventory.objects.get(cabang=cabang)
        return inventory
    except Inventory.DoesNotExist:
        inventory = Inventory.objects.create(
            cabang = cabang
        )
        return inventory

def increaseCabangCreateFunc(product, inventory, quantity):
    ProductInventory.objects.create(
            inventory = inventory,
            product = product,
            stock = quantity
        )

def reduceCabangCreateFunc(product, inventory):
    ProductInventory.objects.create(
            inventory = inventory,
            product = product,
            stock = 0
        )

def increaseOrCreateProductInventory(product, inventory, quantity):
    try:
        productInventory = ProductInventory.objects.get(product=product, inventory=inventory)    
        productInventory.stock=F('stock') + quantity
        productInventory.save()
    except ProductInventory.DoesNotExist:
        increaseCabangCreateFunc(product, inventory, quantity)

def reduceOrCreateProductInventory(product, inventory, quantity):
    productInventory = ProductInventory.objects.get(product=product, inventory=inventory)    
    productDesc = productInventory.product.description
    with transaction.atomic():
        try:
            productInventory.stock = F('stock') - quantity
            productInventory.save()
            productInventory = ProductInventory.objects.get(product=product, inventory=inventory)    
            if productInventory.stock < 0 :
                raise ValueError("Not enough stock for " + productDesc)
        except ProductInventory.DoesNotExist:
            reduceCabangCreateFunc(product, inventory)
        except IntegrityError:
            raise ValueError("Not enough stock for " + productDesc)
    
@receiver(post_save, sender=ProductFaktur, dispatch_uid="add_pusat_inventory")
def incrementPusatInventoryFromProductFaktur(sender, instance, **kwargs):
    incrementPusatInventory(instance.product, instance.quantity)

@receiver(post_save, sender=ProductSalesTransaction, dispatch_uid="reduce_cabang_inventory")
def reduceCabangInventoryFromProductSales(sender, instance, **kwargs):
    cabang = instance.salesTransaction.cabang
    product = instance.product
    quantity = instance.quantity

    reduceCabangInventory(cabang, product, quantity)
    
