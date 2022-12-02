from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('usuarios', views.UsuarioViewSet, basename='usuarios')
router.register('clientes', views.ClienteViewSet, basename='clientes')
router.register('cartoes', views.CartaoViewSet, basename='cartoes')
router.register('enderecos', views.EnderecoViewSet, basename='endereco')
router.register('emprestimos', views.EmprestimoViewSet, basename='emprestimos')
router.register('login', views.LoginViewSet, basename='login')
router.register('pega_cartao', views.PegaCartaoViewSet, basename='pega_cartao')
router.register('usuario_saldo',views.UsuarioAddValueViewSet, basename='usuario_saldo')
urlpatterns = router.urls
