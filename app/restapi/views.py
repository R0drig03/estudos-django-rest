from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TamPizzas, Sabores, Cliente, Pedido
from .serializers import TamPizzasSerializer, ClienteSerializer, PedidoSerializer, SaboresSerializer

#class TamPizzaView(APIView):
#    
#    def get(self, request):
#        model = TamPizzas.objects.all()
#        serializer = TamPizzasSerializer(model, many=True)
#
#        return Response(serializer.data)
#
#
#class ClienteView(APIView):
#    
#    def get(self, request):
#        model = Cliente.objects.all()
#        serializer = ClienteSerializer(model, many=True)
#        
#        return Response(serializer.data)
#    
#
#class SaboresView(APIView):
#
#    def get(self, request):
#        model = Sabores
#        serializer = SaboresSerializer(model, many=True)
#
#        return Response(serializer.data)
#    
#class PedidoView(APIView):
#
#    def get(self, request):
#        model = Pedido
#        serializer = PedidoSerializer(model, many=True)
#
#        return Response(serializer.data)


class TamPizzaViewSet(viewsets.ModelViewSet):
    
    def get(self, request):
        model = TamPizzas.objects.all()
        serializer = TamPizzasSerializer(model, many=True)

        return Response(serializer.data)


class ClienteViewSet(viewsets.ModelViewSet):
    
    def get(self, request):
        model = Cliente.objects.all()
        serializer = ClienteSerializer(model, many=True)
        
        return Response(serializer.data)
    

class SaboresViewSet(viewsets.ModelViewSet):

    def get():
        model = Sabores.objects.all()
        serializer = SaboresSerializer(model, many=True)

        return Response(serializer.data)
    
class PedidoViewSet(viewsets.ModelViewSet):

    def get(self, request):
        model = Pedido.objects.all()
        serializer = PedidoSerializer(model, many=True)

        return Response(serializer.data)