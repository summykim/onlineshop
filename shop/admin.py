from django.contrib import admin

from .models import *
from coupon.models import *

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Catagory,CatagoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category','price','stock','available_display','available_order','created','updated']
    list_filter = ['available_display','category','created','updated']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['price','stock','available_display','available_order']

admin.site.register(Product,ProductAdmin)

class CouponAdmin(admin.ModelAdmin):
    list_display = ['code','use_from','use_to','amount','active']
    list_filter = ['active']
    list_editable = ['use_from','use_to','amount','active']

admin.site.register(Coupon,CouponAdmin)