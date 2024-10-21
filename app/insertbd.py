import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings') 

django.setup()

from restapi.models import Sabores, Cliente, TamPizzas  


#teste = Sabores.objects.all()
#for a in teste:
#    print(a)

teste = Cliente.clientes_niver()
for a in teste:
    print(a)

#sabor = Sabores.objects.create(name_sabor='Bahiana')
#print(sabor)

#cliente = Cliente.objects.create(
#    name_cliente='Rodrigo Vasconcelos do Carmo',
#    cpf_cliente='051.625.652-10',
#    date_aniver=date(2002, 2, 26)
#)

#print(f'DADOS CLIENTE -> {Cliente.()}')


#for a in lista_sabores:
#    print(a)


def insert_tampizza(name_tam_input):
    tam_atual = TamPizzas.objects.create(
        name_tamanho = f'{name_tam_input}'
    )

    print('TAMANHO PIZZA SALVO NO BANCO -> {}'.format(tam_atual))


teste = insert_tampizza('P')
