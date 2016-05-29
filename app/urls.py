from django.conf.urls import url
from app import views

urlpatterns = [
	url(r'^$',views.home),
	url(r'^index',views.home),
	url(r'^textoDescritivo1',views.leiames),
	url(r'^td1s',views.leiame1s),
	url(r'^td2s',views.leiame2s),
	url(r'^td3s',views.leiame3s),
	url(r'^login',views.login),
	url(r'^textoDescritivo',views.leiame),
	url(r'^td1',views.leiame1),
	url(r'^td2',views.leiame2),
	url(r'^td3',views.leiame3),
	url(r'^incluir_cliente',views.incluir_cliente),
	url(r'^incluir_fornecedor',views.incluir_fornecedor),
	url(r'^venda',views.venda),
	url(r'^produto',views.produto),
	url(r'^pedido',views.pedido),
	url(r'^usuario',views.usuario),
]