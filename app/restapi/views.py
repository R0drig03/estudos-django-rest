from rest_framework import viewsets
from rest_framework.views import APIView
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
        model = Pedido.objects.all().select_related('cliente', 'tamanho').prefetch_related('sabores')
        serializer = PedidoSerializer(model, many=True)
        
        return Response(list(serializer.data))



class TratarGetPedido():
    def __init__(self, serializer_dados):
        self.serializer_dados = serializer_dados

    
    
#class TamPizzaViewSet(viewsets.ModelViewSet):    
#    queryset  = TamPizzas.objects.all()
#    serializer = TamPizzasSerializer(queryset, many=True)
#
#
#class ClienteViewSet(viewsets.ModelViewSet):
#    queryset  = Cliente.objects.all()
#    serializer = ClienteSerializer(queryset, many=True)
#    
#    
#class SaboresViewSet(viewsets.ModelViewSet):
#    queryset = Sabores.objects.all()
#    serializer = SaboresSerializer(queryset, many=True)
#
#    
#class PedidoViewSet(viewsets.ModelViewSet):
#    queryset = Pedido.objects.all()
#    serializer = PedidoSerializer(queryset, many=True)
#