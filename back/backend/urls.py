from . import views
from rest_framework_nested import routers   

router = routers.DefaultRouter()
router.register('usuarios', views.UsuarioViewSet, basename='usuarios')
router.register('clientes', views.ClienteViewSet, basename='clientes')
router.register('cartoes', views.CartaoViewSet, basename='cartoes')
router.register('enderecos', views.EnderecoViewSet, basename='endereco')
router.register('transacoes', views.EmprestimoViewSet, basename='transacoes')
urlpatterns = router.urls