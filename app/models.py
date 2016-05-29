from django.db import models

class Email(models.Model):
	descricao = models.CharField(verbose_name='Descrição',max_length=30)
	ativo = models.BooleanField(default=True,verbose_name='Ativo ?')
	
class Endereco(models.Model):
	cep=models.CharField(verbose_name='cep',max_length=30)
	tipo=  models.IntegerField(verbose_name='tipo',default=0)
	descricao = models.CharField(verbose_name='descricao',max_length=30)
	complemento = models.CharField(verbose_name='complemento',max_length=30)
	numero =  models.IntegerField(verbose_name='numero',default=0)
	ativo = models.IntegerField(verbose_name='ativo',default=0)
	endereco = models.Manager()	
	
class Documento(models.Model):
	numero= models.IntegerField(verbose_name='numero',default=0)
	tipo = models.IntegerField(verbose_name='tipo',default=0)
	emissao=models.DateField(verbose_name='emissao') 
	vencimento = models.DateField(verbose_name='vencimennto')
	ativo=models.IntegerField(verbose_name='ativo',default=0)
	endereco= models.ForeignKey(Endereco, on_delete = models.CASCADE)
	email = models.ForeignKey(Email, on_delete = models.CASCADE)
	documento=models.Manager()
	
class Cliente(models.Model):
	nome = models.CharField(verbose_name='nome',max_length=30)
	telefone= models.IntegerField(verbose_name='telefone',default=0)
	foto = models.ImageField(upload_to='cliente/', height_field=None, width_field=None, max_length=100,blank=True,null=True,default='cliente/no_foto.jpg')
	documento = models.ForeignKey(Documento, on_delete = models.CASCADE)
	cliente=models.Manager()
	
class Fornecedor(models.Model):
	nome = models.CharField(verbose_name='nome',max_length=30)
	foto = models.ImageField(upload_to='cliente/', height_field=None, width_field=None, max_length=100,blank=True,null=True,default='cliente/no_foto.jpg')
	telefone= models.IntegerField(verbose_name='telefone',default=0)
	documento = models.ForeignKey(Documento, on_delete = models.CASCADE)
	produto= models.CharField(verbose_name='nome',max_length=30)
	fornecedor = models.Manager()
	
class Financeiro(models.Model):
	entidade= models.CharField(verbose_name='entidade',max_length=30)
	valor = models.DecimalField(max_digits=15, decimal_places=2)
	desconto = models.DecimalField(max_digits=15, decimal_places=2)
	valor_pago =models.DecimalField(max_digits=15, decimal_places=2)
	
class Unidade(models.Model):
	descricao = models.CharField(verbose_name='descricao',max_length=30)
	fator= models.IntegerField(verbose_name='fator',default=0)

class Produto(models.Model):
	foto = models.ImageField(upload_to='produto/', height_field=None, width_field=None, max_length=100,blank=True,null=True,default='produto/no_foto.jpg')
	descricao = models.CharField(verbose_name='descricao',max_length=30)
	unidade = models.ForeignKey(Unidade, on_delete = models.CASCADE)
	estoque = models.IntegerField(verbose_name='estoque',default=0)

class Configuracao(models.Model):
	quantidade_parcela = models.IntegerField(verbose_name='quantidade_parcela',default=0)
	
class Item(models.Model):
	produto = models.ForeignKey(Produto, on_delete = models.CASCADE)
	quantidade = models.IntegerField(verbose_name='quantidade',default=0)
	valor = models.DecimalField(verbose_name = 'Valor', max_digits = 15, decimal_places = 2, default=0 )
 
class Pedido(models.Model):
	item = models.ForeignKey(Item, on_delete = models.CASCADE)
	configuracao = models.ForeignKey(Configuracao, on_delete = models.CASCADE)
	
class Venda(models.Model):
	item = models.ForeignKey(Item, on_delete = models.CASCADE)
	financeiro= models.ForeignKey(Financeiro, on_delete = models.CASCADE)
	configuracao = models.ForeignKey(Configuracao, on_delete = models.CASCADE)
	



	
	
	
	
	
	
	
	
	
	
	
	