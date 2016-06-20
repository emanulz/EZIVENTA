# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from.models import Product
from.models import ProductDepartment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_description', 'product_code', 'product_sellmethod', 'product_sellprice', )


@admin.register(ProductDepartment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('productdepartment_name', )
