# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Product (models.Model):

    Unit = 'uni'
    Bulk = 'bul'
    Kit = 'kit'

    SELLS_CHOICES = ((Unit, 'Por Unidad'),
                     (Bulk, 'A Granel'),
                     (Kit, 'En Paquete(kit)'),
                     )

    product_description = models.CharField(max_length=255, verbose_name='Descripción del producto', default=' ')
    product_code = models.IntegerField(verbose_name='Código', unique=True, default=0)
    product_barcode = models.IntegerField(verbose_name='Código de Barras', blank=True, default=0)
    product_department = models.ForeignKey('ProductDepartment', default=1, verbose_name='Departamento')
    product_useinventory = models.BooleanField(default=False, verbose_name='Sistema de Inventarios?')
    product_inventory = models.FloatField(default=0, verbose_name='Existencia en Inventario')
    product_minimum = models.FloatField(default=0, verbose_name='Mínimo en inventario')
    product_sellmethod = models.CharField(max_length=3, choices=SELLS_CHOICES, default=Unit,
                                          verbose_name='Se Vende Por')
    product_cost = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Costo ₡')
    product_autoprice = models.BooleanField(default=False, verbose_name='Precio Automático?')
    product_utility = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name='Utilidad %')
    product_price = models.DecimalField(default=0, max_digits=10, decimal_places=2,
                                        verbose_name='Precio sin Impuestos ₡')
    product_usetaxes = models.BooleanField(default=False, verbose_name='Usa Impuestos?')
    product_taxes = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name='Impuestos %')
    product_sellprice = models.DecimalField(default=0, max_digits=10, decimal_places=2,
                                            verbose_name='Precio de Venta ₡')

    def __unicode__(self):
        return '%s' % self.product_description

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = '1. Productos'
        ordering = ['product_code']


class ProductDepartment(models.Model):

    productdepartment_name = models.CharField(max_length=255, verbose_name='Nombre del Departamento', unique=True)

    def __unicode__(self):
        return '%s' % self.productdepartment_name

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = '2. Departamentos'
        ordering = ['productdepartment_name']
