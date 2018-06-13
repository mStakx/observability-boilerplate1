from django.db import models
from django_prometheus.models import ExportModelOperationsMixin

class Pizza(ExportModelOperationsMixin('pizza'), models.Model):
    name = models.CharField(max_length=100, unique=True)
    size = models.PositiveIntegerField(blank=True, null=True)
    cost = models.PositiveIntegerField(blank=True, null=True)

class Order(ExportModelOperationsMixin('order'), models.Model):
    order_id = models.AutoField(primary_key=True)
    cost = models.PositiveIntegerField(blank=True, null=True)