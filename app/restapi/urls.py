from django.urls import path, include

#from .views import TamPizzaViewSet, ClienteViewSet, PedidoViewSet, SaboresViewSet
from django.contrib import admin
from rest_framework.routers import DefaultRouter

#MANEIRA DE DEFINIR AS URLS CASO NAS VIEWS EU ESTEJA USANDO O "APIView" para declarar cada endpoint

from .views import TamPizzaView, ClienteView, PedidoView, SaboresView, BasicView
urlpatterns = [
    path('tamanho/', TamPizzaView.as_view(), name='Tamanho Pizzas'),
    path('cliente/', ClienteView.as_view(), name='cliente'),
    path('sabores/', SaboresView.as_view(), name='sabores'),
    path('pedidos/', PedidoView.as_view(), name='pedidos'),
    path('admin/', admin.site.urls),
    path('basic/', BasicView, name='basic')
]


#MANEIRA DE DEFINIR AS URLS CASO NAS VIEWS EU ESTEJA USANDO O "ModelViewSet" para declarar os meus endpoints

#router = DefaultRouter()
#router.register(r'tamanho', TamPizzaViewSet)
#router.register(r'cliente', ClienteViewSet)
#router.register(r'pedidos', PedidoViewSet)
#router.register(r'sabores', SaboresViewSet)
#
#urlpatterns = [
#    path('admin/', admin.site.urls),  # Mantendo o admin com a barra final
#    path('', include(router.urls)),  # Inclui todas as rotas geradas pelo router
#]