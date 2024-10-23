from rest_framework import serializers
from .models import TamPizzas, Cliente, Pedido, Sabores
from django.utils import timezone

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


class SaboresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sabores
        fields = ['id', 'name_sabor', 'created_at']

        #extra_kwargs = {
        #    'id': {'write_only': True}   #---> FUNÇÃO PARA PROTEGER ALGUNS CAMPOS QUE NÃO VÃO SER APRESENTADOS NO SWAGGER DA API
        #}

class PedidoSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.CharField(source='fgkey_cliente.name_cliente')
    tamanho = serializers.CharField(source='fgkey_tam.name_tamanho')
    sabor = serializers.CharField(source='fgkey_sabor.name_sabor')
    tempo_desde_pedido = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = ['id', 'cliente_nome', 'tamanho', 'sabor', 'number_mesa', 'created_at', 'tempo_desde_pedido']

    def get_tempo_desde_pedido(self, obj):
        tempo_decorrido = timezone.now() - obj.created_at
        return f"{tempo_decorrido.days} dias, {tempo_decorrido.seconds // 3600} horas"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            "pedido_id": representation['id'],
            "cliente": representation['cliente_nome'],
            "detalhes": {
                "tamanho": representation['tamanho'],
                "sabor": representation['sabor'],
                "mesa": representation['number_mesa']
            },
            "data_pedido": representation['created_at'],
            "tempo_desde_pedido": representation['tempo_desde_pedido']
        }









