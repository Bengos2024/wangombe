from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=['code','name','price','stock','image_url']

admin.site.register(Product,ProductAdmin)
