# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from resapp.models import Product, Order

admin.site.register(Product)
admin.site.register(Order)
