import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings') 

django.setup()

from restapi.models import Sabores, Cliente  

#sabor = Sabores.objects.create(name_sabor='Bahiana')
#print(sabor)

cliente = Cliente.objects.create(
    name_cliente='Rodrigo Vasconcelos do Carmo',
    cpf_cliente='051.625.652-10',
    date_aniver=date(2002, 2, 26)
)

print(f'DADOS CLIENTE -> {cliente.get_cliente()}')


#for a in lista_sabores:
#    print(a)