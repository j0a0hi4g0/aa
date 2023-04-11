from django.db import models

class compras(models.Model):
    lista = models.CharField(max_length=64)
    valor = models.CharField(max_length=64)


