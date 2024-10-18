import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings') 

django.setup()

from models import Sabores  

sabor = Sabores.objects.create(name_sabor='Calabresa')
print('DADOS SALVOS NO BANCO')
