from rest_framework import serializers
from .models import TamPizzas, Cliente, Pedido, Sabores


class TamPizzasSerializer(serializers.ModelSerializer):
    class Meta:
        model = TamPizzas
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
       
    class Meta:
        extra_kwargs = {
            'cpf_cliente': {'write_only': True}   #---> FUNÇÃO PARA PROTEGER ALGUNS CAMPOS QUE NÃO VÃO SER APRESENTADOS NO SWAGGER DA API
        }

        model = Cliente
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'


class SaboresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sabores
        fields = '__all__'



