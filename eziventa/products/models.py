# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Product (models.Model):

    code = models.IntegerField(verbose_name='Código')
    description = models.CharField(max_length=255)
