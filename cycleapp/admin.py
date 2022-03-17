from django.contrib import admin
from cycleapp.models import Cycle,Cart,Order_in_Progress,Order_Done
# Register your models here.

@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
    list_display = ('id','sellor','bike_name','date_sell','brand','category','description','bike_image','stock','price','discount','date_sell','total_sold','delivery_time')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id','user','cycle','quantity')

@admin.register(Order_in_Progress)
class Order_in_ProgressAdmin(admin.ModelAdmin):
    list_display = ('id','user','cycle','quantity','total_payment','user_phone','shipping_address','payment_method','order_date','delivery_date')

@admin.register(Order_Done)
class Order_DoneAdmin(admin.ModelAdmin):
    list_display = ('id','user','cycle','quantity')