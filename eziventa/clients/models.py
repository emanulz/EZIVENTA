# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Client(models.Model):

    SinId = 'noid'
    Nacional = 'naci'
    Passaporte = 'pass'
    Juridica = 'juri'

    ID_CHOICES = ((SinId,'Sin Identificación'),
                  (Nacional,'Cédula Nacional'),
                  (Passaporte,'Número de Pasaporte'),
                  (Juridica,'Cédula Jurídica')
                  )

    client_name = models.CharField(max_length=255, verbose_name='Nombre')
    client_last_name = models.CharField(max_length=255, blank=True, verbose_name='Apellidos')
    client_id_type = models.CharField(max_length=4, choices=ID_CHOICES, default=SinId,
                                      verbose_name='Tipo de Identificación')
    client_id = models.PositiveIntegerField(blank=True, verbose_name='Identificación')
    client_address = models.CharField(max_length=255, blank=True, verbose_name='Dirección')
    client_email = models.EmailField(verbose_name='Email', blank=True)
    client_phone_number = models.DecimalField(max_digits=8, decimal_places=0, blank=True, verbose_name='Teléfono')

    def __unicode__(self):
        return '%s %s' % (self.client_name, self.client_last_name)

    class Meta:

        ordering = ['id']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

