from django.db.models.signals import post_save
from django.dispatch import receiver
from pos.models import ProductFaktur
from pos.inventorymodels import Inventory, ProductInventory, PusatProductInventory
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

# @receiver(post_save, sender=ProductFaktur, dispatch_uid="add_cabang_inventory")
# def updateCabangInventory(sender, instance, **kwargs):
#     print('post save inventory ' + str(instance))
#     cabang = instance.faktur.cabang
#     try:
#         inventory = Inventory.objects.get(cabang=cabang)
#     except Inventory.DoesNotExist:
#         inventory = None

#     if inventory is None:
#         inventory = Inventory.objects.create(
#             cabang = cabang
#         )

#     try:
#         productInventory = ProductInventory.objects.get(product=instance.product, inventory=inventory)    
#         ProductInventory.objects.filter(product=productInventory.product).update(stock=F('stock') + instance.quantity) 
#     except ProductInventory.DoesNotExist:
#         ProductInventory.objects.create(
#             inventory = inventory,
#             product = instance.product,
#             stock = instance.quantity
#         )

    
