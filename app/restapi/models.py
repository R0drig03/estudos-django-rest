from typing import Any
from django.db import models
from datetime import datetime


def trate_timezone(timz: datetime):
    dt_with_timezone = datetime.strptime(str(timz), "%Y-%m-%d %H:%M:%S.%f %z")

    dt_normal = dt_with_timezone.replace(tzinfo=None, microsecond=0)

    return dt_normal


class Sabores(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_sabor = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __init__(self) -> list:
        return list(self.id, self.name_sabor, self.created_at)


class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_cliente = models.CharField(max_length=255)
    cpf_cliente = models.CharField(max_length=14)
    date_aniver = models.DateField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def get_cliente(self) -> list:
        return [self.id, self.name_cliente, self.cpf_cliente, self.date_aniver, f'{self.created_at}']

    @classmethod
    def clientes_niver(cls):
        #return [x for x in list(cls.objects.all()) if datetime.strptime(str(x[3]), '') == datetime.today()]
        pass


#class tamanho_pizzas(models.Model):
#    TAM_CHOICES = {
#        '1': 'Pequena',
#        '2': 'Média',
#        '3': 'Grande',
#        '4': 'Extra Grande',
#        '5': 'Família'
#    }
#
#    id = models.BigAutoField(primary_key=True)
#    tamanho = models.Choices(max_length=1, choices=TAM_CHOICES)
#
#
#
#class mesas(models.Model):
#    id_mesa = models.BigAutoField(primary_key=True)
#
#
#class pedidos(models.Model):
#    pass
#