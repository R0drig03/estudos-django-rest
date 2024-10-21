from rest_framework import serializers
from .models import TamPizzas, Cliente, Pedido, Sabores


class TamPizzasSerializer(serializers.ModelSerializer):
    class Meta:
        #extra_kwargs = {
        #    'id': {'write_only': True}   ---> FUNÇÃO PARA PROTEGER ALGUNS CAMPOS QUE NÃO VÃO SER APRESENTADOS NO SWAGGER DA API
        #}

        model = TamPizzas
        fields = (
            'id',
            'name_tamanho'    
        )


class ClienteSerializer(serializers.ModelSerializer):
    extra_kwargs = {
            'cpf_cliente': {'write_only': True},   #---> FUNÇÃO PARA PROTEGER ALGUNS CAMPOS QUE NÃO VÃO SER APRESENTADOS NO SWAGGER DA API
            'created_at': {'write_only': True}
        }
        
    class Meta:
        model = TamPizzas
        fields = (
            'id',
            'name_cliente',
            'cpf_cliente',
            'date_aniver',
            'created_at'    
        )


class PedidoSerializer(serializers.ModelSerializer):
    pass

class SaboresSerializer(serializers.ModelSerializer):
    pass
