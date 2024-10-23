from typing import Any
from django.db import models
from datetime import date


class TamPizzas(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_tamanho = models.CharField(max_length=2)

    def __str__(self):
        return '{}'.format(self.name_tamanho)

    

class Sabores(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_sabor = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '{}'.format(self.name_sabor)


class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_cliente = models.CharField(max_length=255)
    cpf_cliente = models.CharField(max_length=14)
    date_aniver = models.DateField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return '{}. {}'.format(self.id, self.name_cliente)

    @classmethod
    def clientes_niver(cls): # -> CLS = MODEL ATUAL     
        return cls.objects.filter(
            date_aniver__month=date.today().month,
            date_aniver__day=date.today().day
        )


class Pedido(models.Model):
    id = models.BigAutoField(primary_key=True)
    fgkey_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    fgkey_sabor = models.ForeignKey(Sabores, on_delete=models.CASCADE, verbose_name='Sabor')
    fgkey_tam = models.ForeignKey(TamPizzas, on_delete=models.CASCADE, verbose_name='Tamanho')
    number_mesa = models.IntegerField(verbose_name='Número da Mesa', )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self) -> str:
        return f'DADOS SALVOS -> {self.id}. {self.fgkey_cliente.name_cliente}. {self.fgkey_sabor.name_sabor}. {self.fgkey_tam.name_tamanho}. {self.number_mesa}. {self.created_at}'

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