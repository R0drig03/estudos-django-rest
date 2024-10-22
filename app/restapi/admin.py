from django.contrib import admin
from .models import Cliente, Pedido, TamPizzas, Sabores

# Registre os modelos no admin
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(TamPizzas)
admin.site.register(Sabores)