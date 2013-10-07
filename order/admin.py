from django.contrib import admin

from models import Product,Ptype,Order,UserProfile


admin.site.register(Product)
admin.site.register(Ptype)
admin.site.register(Order)
admin.site.register(UserProfile)