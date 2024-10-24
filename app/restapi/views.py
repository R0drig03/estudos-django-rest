from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TamPizzas, Sabores, Cliente, Pedido
from .serializers import TamPizzasSerializer, ClienteSerializer, PedidoSerializer, SaboresSerializer

class TamPizzaView(APIView):
    
    def get(self, request):
        model = TamPizzas.objects.all()
        serializer = TamPizzasSerializer(model, many=True)

        return Response(serializer.data)


class ClienteView(APIView):
    
    def get(self, request):
        model = Cliente.objects.all()
        serializer = ClienteSerializer(model, many=True)
        
        return Response(serializer.data)
    

class SaboresView(APIView):

    def get(self, request):
        model = Sabores.objects.all()
        serializer = SaboresSerializer(model, many=True)

        return Response(serializer.data)
    
class PedidoView(APIView):

    def get(self, request):
        model = Pedido.objects.select_related('fgkey_cliente', 'fgkey_tam')\
                                .prefetch_related('fgkey_sabor').all()


        serializer = PedidoSerializer(model, many=True)
        
        return Response(serializer.data)

    def post(self, request):        
        data = request.data

        try:
            cliente = Cliente.objects.get(id=data.get('fgkey_cliente'))
            tamanho = TamPizzas.objects.get(id=data.get('fgkey_tam'))
            sabores = Sabores.objects.filter(id__in=data.get('fgkey_sabor', []))
            
            print('DADOS DE ENTRADA -> {} -> {} -> {}'.format(cliente, tamanho, sabores))
        
        except Cliente.DoesNotExist:
            return Response({"error": "Cliente não encontrado."}, status=404)
        except TamPizzas.DoesNotExist:
            return Response({"error": "Tamanho não encontrado."}, status=404)
        except Sabores.DoesNotExist:
            return Response({"error": "Um ou mais sabores não foram encontrados."}, status=404)

        pedido = Pedido(
            fgkey_cliente=cliente,
            fgkey_tam=tamanho
        )
        pedido.save()

        pedido.fgkey_sabor.set(sabores)

        serializer = PedidoSerializer(pedido)
        
        return Response(serializer.data, status=201)
        
@api_view()
def BasicView(request):
    return Response('Testando uma maneira de declarar uma view de maneira mais simples.')

