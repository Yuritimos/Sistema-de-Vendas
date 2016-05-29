from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader
	
def home(request):
	template=loader.get_template('index.html')
	context=RequestContext(request)
	return HttpResponse(template.render(context))	

def usuario(request):
	template=loader.get_template('usuario.html')
	context=RequestContext(request)
	return HttpResponse(template.render(context))	
	
def leiame(request):
	template=loader.get_template('textoDescritivo.html')
	context=RequestContext(request)
	return HttpResponse(template.render(context))
	
def leiame1(request):
	template=loader.get_template('td1.html')
	context=RequestContext(request)
	return HttpResponse(template.render(context))
	
def leiame2(request):
	template=loader.get_template('td2.html')
	context=RequestContext(request)
	return HttpResponse(template.render(context))
	
def leiame3(request):
	template=loader.get_template('td3.html')
	context=RequestContext(request)
	return HttpResponse(template.render(context))
	
def leiames(request):
	template=loader.get_template('textoDescritivo1.html')
	context=RequestContext(request)
	return HttpResponse(template.render(context))
	
def leiame1s(request):
	template=loader.get_template('td1s.html')
	context=RequestContext(request)
	return HttpResponse(template.render(context))
	
def leiame2s(request):
	template=loader.get_template('td2s.html')
	context=RequestContext(request)
	return HttpResponse(template.render(context))
	
def leiame3s(request):
	template=loader.get_template('td3s.html')
	context=RequestContext(request)
	return HttpResponse(template.render(context))
	
def login(request):
	template=loader.get_template('login.html')
	context=RequestContext(request)
	return HttpResponse(template.render(context))
	
def incluir_cliente(request):
	template=loader.get_template('incluir_cliente.html')
	context=RequestContext(request)
	return HttpResponse(template.render(context))
	
def incluir_fornecedor(request):
	template=loader.get_template('incluir_fornecedor.html')
	context=RequestContext(request)
	return HttpResponse(template.render(context))
	
def venda(request):
	template=loader.get_template('venda.html')
	context=RequestContext(request)
	return HttpResponse(template.render(context))
	
def produto(request):
	template=loader.get_template('produto.html')
	context=RequestContext(request)
	return HttpResponse(template.render(context))
	
def pedido(request):
	template=loader.get_template('pedido.html')
	context=RequestContext(request)
	return HttpResponse(template.render(context))
	
	
	
	
	
	
	
	
	
	




	
	
	