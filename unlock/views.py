from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordResetForm


from django.http import HttpResponse
#from django.template import loader


from .models import Lampada
##################
from .models import Botao
from .models import Status
from .models import Registrobotao
##################
from .models import Porta
from .models import User
from .models import Setor
from .models import Pessoas
from .models import Acesso
from .models import Registro
#############################
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
##########################
#from django.shortcuts import render
#from django.utils.safestring import mark_safe
#import json

def entrar(request):
	return render(request, 'unlock/entrar.html',)

def login_controller(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
       	return redirect('index')
    else:
        return HttpResponse ("Login invalido")

def novo_usuario(request):
	return render(request,'unlock/novo_usuario.html',)

def novo_usuario_controller(request):
	username = request.POST['username']
	email = request.POST['email']
	psw = request.POST['psw']
	pswrepeat = request.POST['pswrepeat']
	if psw==pswrepeat:
		contador1 = User.objects.filter(email= email).count()
		contador2 = User.objects.filter(username= username).count()
		if contador1==0 and contador2==0:
			User.objects.create_user(username= username,email = email,password = psw)
#			User(username= username,email = email,password = psw).save()
			return redirect('entrar')
		else:
			return redirect('erro')
	else:
		return redirect('erro')



def logout_controller(request):
    logout(request)
    return redirect('entrar')

def teste(request):
    if not request.user.is_authenticated():
        return render(request, 'unlock/erro.html')
    return render(request, 'unlock/teste.html',)

def index(request):
	if not request.user.is_authenticated:
		return render(request, 'unlock/entrar.html')
	contador_pessoas = Pessoas.objects.filter(usuario = request.user).count()
	contador_portas = Porta.objects.filter(usuario = request.user).count()
	contador_registros_liberados = Registro.objects.filter(permissao = True,usuario = request.user).count()
	contador_registros_bloqueados = Registro.objects.filter(permissao = False,usuario = request.user).count()
	lista = Registro.objects.filter(usuario = request.user).order_by('-data_acesso') [:6]
	return render(request, 'unlock/index.html',{'contador_pessoas':contador_pessoas, 'contador_portas':contador_portas, 'contador_registros_liberados':contador_registros_liberados, 'contador_registros_bloqueados':contador_registros_bloqueados, 'lista':lista})

#def index(request):
#	contador_pessoas = Pessoas.objects.count()
#	contador_portas = Porta.objects.count()
#	contador_registros_liberados = Registro.objects.filter(permissao = True).count()
#	contador_registros_bloqueados = Registro.objects.filter(permissao = False).count()
#	lista = Registro.objects.order_by('-data_acesso') [:6]
#	return render(request, 'unlock/index.html',{'contador_pessoas':contador_pessoas, 'contador_portas':contador_portas, 'contador_registros_liberados':contador_registros_liberados, 'contador_registros_bloqueados':contador_registros_bloqueados, 'lista':lista})

def meuusuario(request):
	if not request.user.is_authenticated:
		return render(request, 'unlock/entrar.html')
	return render(request, 'unlock/meuusuario.html')

def alterar_usuario(request):
	if not request.user.is_authenticated:
		return render(request, 'unlock/entrar.html')
	return render(request, 'unlock/alterar_usuario.html')

def alterar_usuario_controller(request):
	username = request.POST['username']
	nome = request.POST['nome']
	sobrenome = request.POST['sobrenome']
	email = request.POST['email']
	contador = User.objects.filter(username=username).count()
	contador2 = User.objects.filter(email=email).count()

	if (contador == 0 and contador2 == 0) or (contador == 1 and contador2 == 0 and username==request.user.username) or (contador == 0 and contador2 == 1 and email==request.user.email) or (contador == 1 and contador2 == 1 and request.user.username and email==request.user.email):
		User.objects.filter(username=request.user).update(username=username,first_name = nome, last_name = sobrenome, email = email)
		return redirect('index')
	else:
		return HttpResponse ("Username ou email já utilizado.")

def porta(request):
	if not request.user.is_authenticated:
		return render(request, 'unlock/entrar.html')
	lista = Porta.objects.filter(usuario = request.user).order_by('numero_porta') #[:5]
	context = {'lista': lista}
	return render(request, 'unlock/porta.html', context)

def infoporta(request, porta_id):
	if not request.user.is_authenticated:
		return render(request, 'unlock/entrar.html')
	informacao = get_object_or_404(Porta, pk=porta_id)
	lista = Acesso.objects.filter(porta=porta_id,usuario = request.user)
	return render(request, 'unlock/infoporta.html', {'lista': lista,'informacao': informacao})    

def add_setor(request):
	return render(request, 'unlock/add_setor.html')

def add_setor_controller(request):
	nomesetor = request.POST['nomesetor']
	contador = Setor.objects.filter(nome_setor=nomesetor, usuario = request.user).count()
	if contador == 0:
		Setor(nome_setor=nomesetor, usuario = request.user).save()
		return redirect('index')
	else:
		return HttpResponse ("Setor já cadastrado.")	


def add_porta(request):
	if not request.user.is_authenticated:
		return render(request, 'unlock/entrar.html')
	lista = Setor.objects.filter(usuario = request.user).order_by('nome_setor') #[:5]
	context = {'lista': lista}
	return render(request, 'unlock/add_porta.html', context)

def add_porta_controller(request):
	codigo_porta = request.POST['codigo_porta']
	numero_porta = int(request.POST['numeroporta'])
	descricao_porta = request.POST['descricaoporta']
	setordaporta = request.POST['selectsetor']
	contador = Porta.objects.filter(numero_porta=numero_porta, usuario = request.user).count()
	contador2 = Porta.objects.filter(codigo_porta=codigo_porta).count()
	if contador == 0 and contador2 == 0:
		if setordaporta == '':
			Porta(numero_porta=numero_porta,descricao_porta=descricao_porta,usuario = request.user).save()
			return redirect('index')
		else:
			Porta(numero_porta=numero_porta,descricao_porta=descricao_porta, setor_porta= Setor.objects.get(id=setordaporta),usuario = request.user).save()
			return redirect('index')
	else:
		return HttpResponse ("Número ou codigo da porta já cadastrado.")
	#return render(request, 'unlock/add_porta_controller.html', {'setor_porta' : setor_porta})

def pessoa(request):
	if not request.user.is_authenticated:
		return render(request, 'unlock/entrar.html')
	lista = Pessoas.objects.filter(usuario = request.user).order_by('nome_pessoa') #[:5]
	context = {'lista': lista}
	return render(request, 'unlock/pessoa.html', context)

def infopessoa(request, pessoas_id):
	if not request.user.is_authenticated:
		return render(request, 'unlock/entrar.html')
	informacao = get_object_or_404(Pessoas, pk=pessoas_id)
	lista = Acesso.objects.filter(pessoa=pessoas_id,usuario = request.user).order_by('porta__numero_porta')
	return render(request, 'unlock/infopessoa.html', {'lista': lista,'informacao': informacao})

def add_pessoa(request):
	if not request.user.is_authenticated:
		return render(request, 'unlock/entrar.html')
	lista = Setor.objects.filter(usuario = request.user).order_by('id') #[:5]
	context = {'lista': lista}
	return render(request, 'unlock/add_pessoa.html', context)

def add_pessoa_controller(request):
	nome_pessoa =request.POST['nomepessoa']
	cpf = request.POST['cpf']
	setorpessoa = request.POST['selectsetor']
	codigo_cartao = request.POST['codigocartao']
	email = request.POST['email']
	contador = Pessoas.objects.filter(cpf=cpf,usuario = request.user).count()
	contador2 = Pessoas.objects.filter(codigo_cartao=codigo_cartao,usuario = request.user).count()
	contador3 = Porta.objects.filter(setor_porta=setorpessoa,usuario = request.user).count()
	vetor = [contador3]
#	if contador == 0 and contador2 == 0:
#		Pessoas(nome_pessoa=nome_pessoa,cpf=cpf,codigo_cartao=codigo_cartao, setor_pessoa= Setor.objects.get(id=setorpessoa), email=email).save()
#		Acesso(pessoa= Pessoas.objects.get(nome_pessoa=nome_pessoa),porta= Porta.objects.get(setor_porta=setorpessoa),permissao_acesso = False).save()
#		return redirect('index')
#	else:
#		return HttpResponse ("Cpf ou cartão ja cadastrado")

	if contador == 0 and contador2 == 0:
		Pessoas(nome_pessoa=nome_pessoa,cpf=cpf,codigo_cartao=codigo_cartao, setor_pessoa= Setor.objects.get(id=setorpessoa), email=email,usuario = request.user).save()
		return redirect('index')
	else:
		return HttpResponse ("Cpf ou cartão ja cadastrado")

def teste(request):
    if not request.user.is_authenticated:
        return render(request, 'unlock/erro.html')
    return render(request, 'unlock/teste.html',)

#def teste(request):
#	return render(request, 'unlock/teste.html',)

def erro(request):
	return render(request, 'unlock/erro.html',)

def add_acesso(request):
	if not request.user.is_authenticated:
		return render(request, 'unlock/entrar.html')
	lista = Porta.objects.filter(usuario = request.user).order_by('numero_porta')
	lista2 = Pessoas.objects.filter(usuario = request.user).order_by('nome_pessoa')
	return render(request, 'unlock/add_acesso.html', {'lista2': lista2,'lista': lista})

def add_acesso_controller(request):
	porta = request.POST['selectporta']
	pessoa = request.POST['selectpessoa']
	contador = Acesso.objects.filter(pessoa= Pessoas.objects.get(id=pessoa),porta= Porta.objects.get(id=porta),usuario = request.user).count()
	if contador==0:
		Acesso(pessoa= Pessoas.objects.get(id=pessoa),porta= Porta.objects.get(id=porta),usuario = request.user).save()
		return redirect('index')
	else:
		return HttpResponse ("Acesso já cadastrado")

def blq_acesso_controller(request):
	acesso = request.POST['acesso']
	Acesso.objects.filter(id=acesso,usuario = request.user).update(permissao_acesso=False)
	return redirect('pessoa')

def desblq_acesso_controller(request):
	acesso = request.POST['acesso']
	Acesso.objects.filter(id=acesso,usuario = request.user).update(permissao_acesso=True)
	return redirect('pessoa')

def registro(request):
	if not request.user.is_authenticated:
		return render(request, 'unlock/entrar.html')
	lista = Porta.objects.filter(usuario = request.user).order_by('numero_porta')
	lista2 = Pessoas.objects.filter(usuario = request.user).order_by('nome_pessoa')
	return render(request, 'unlock/registro.html',{'lista2': lista2,'lista': lista})

def relatorio_registro(request):
	if not request.user.is_authenticated:
		return render(request, 'unlock/entrar.html')
	pessoa_id = request.POST['selectpessoar']
	porta_id = request.POST['selectportar']
	datai = request.POST['datei']
	dataf = request.POST['datef']
	#return HttpResponse (contador)
	if porta_id == '' and pessoa_id == '':
		lista = Registro.objects.filter(data_acesso__lte=dataf, data_acesso__gte=datai,usuario = request.user).order_by('-data_acesso') #[:5]
	elif porta_id == '':
		lista = Registro.objects.filter(pessoa = pessoa_id,usuario = request.user).order_by('-data_acesso') #[:5]
	elif pessoa_id == '' :
		lista = Registro.objects.filter(porta_acessada = porta_id,usuario = request.user).order_by('-data_acesso') #[:5]
	else:
		lista = Registro.objects.filter(pessoa = pessoa_id, porta_acessada = porta_id,usuario = request.user).order_by('-data_acesso') #[:5]
#	return HttpResponse (datai)
	return render(request, 'unlock/relatorio_registro.html', {'lista': lista})

def relatorio_registro_pessoa(request):
	pessoa_id = request.POST['selectpessoa']
	lista = Registro.objects.filter(acesso__pessoa = pessoa_id).order_by('-data_acesso')
	return render(request, 'unlock/relatorio_registro_pessoa.html',{'lista': lista})

def relatorio_registro_porta(request):
	porta_id = request.POST['selectporta']
	lista = Registro.objects.filter(acesso__porta = porta_id).order_by('-data_acesso')
	return render(request, 'unlock/relatorio_registro_pessoa.html',{'lista': lista})

def acesso_controller (request, porta, carteira): 

	try:
		contador = Acesso.objects.filter(pessoa= Pessoas.objects.get(codigo_cartao=carteira),porta= Porta.objects.get(codigo_porta=porta),permissao_acesso= True).count()


		if contador == 1:
			info = Pessoas.objects.get(codigo_cartao=carteira)
			usuar = info.usuario
			Registro(acesso = Acesso.objects.get(pessoa= Pessoas.objects.get(codigo_cartao=carteira),porta= Porta.objects.get(codigo_porta=porta),),
			pessoa = Pessoas.objects.get(codigo_cartao=carteira),
			porta_acessada= Porta.objects.get(codigo_porta=porta),
			codigo_recebido = carteira,
			permissao = True,
			usuario = usuar
			).save()
			return HttpResponse (contador)
		else:
			info = Pessoas.objects.get(codigo_cartao=carteira)
			usuar = info.usuario
			Registro(
			pessoa= Pessoas.objects.get(codigo_cartao=carteira),
			porta_acessada= Porta.objects.get(codigo_porta=porta),
			codigo_recebido = carteira,
			permissao = False,
			usuario = usuar
			).save()
			return HttpResponse (contador)

	except ObjectDoesNotExist:
		info = Porta.objects.get(codigo_porta=porta)
		usuar = info.usuario
		Registro(
		porta_acessada= Porta.objects.get(codigo_porta=porta),
		codigo_recebido = carteira,
		permissao = False,
		usuario = usuar
		).save()
		return HttpResponse ("0")
#    ...
#	return HttpResponse("1")
#	return HttpResponse("Porta %s" % contador)
#	return redirect('index')

########################################################
def indexpanicbutton(request):
	lista = Botao.objects.order_by('nome_botao') #[:5]
	alerta = Botao.objects.filter(situacao = 2).order_by('nome_botao') #[:5]
#	return HttpResponse("Botão %s" % alerta)
	return render(request, 'unlock/indexpanicbutton.html', {'alerta': alerta,'lista': lista})

def paginadiego(request):
	alerta = Botao.objects.filter(situacao = 2).order_by('nome_botao') #[:5]
	return render(request, 'unlock/paginadiego.html', {'alerta': alerta})

def infobotao(request, botao_id):
	informacao = get_object_or_404(Botao, pk=botao_id)
	return render(request, 'unlock/infobotao.html', {'informacao': informacao})    

def add_botao(request):
	return render(request, 'unlock/add_botao.html')

def add_botao_controller(request):
	nome_botao =request.POST['nome_botao']
	endereco_botao = request.POST['endereco_botao']
	cep = request.POST['cep']
	email_botao = request.POST['email_botao']
	telefone_botao = request.POST['telefone_botao']
	key_botao = request.POST['key_botao']
	contador = Botao.objects.filter(key_botao=key_botao).count()
	if contador == 0:
		Botao(nome_botao=nome_botao,endereco_botao=endereco_botao,cep=cep, email_botao= email_botao, telefone_botao=telefone_botao,key_botao = key_botao).save()
		return redirect('indexpanicbutton')
	else:
		return HttpResponse ("Dispositivo já cadastrado")

def normalizar(request):
		botao = request.POST['botao']
		Botao.objects.filter(id=botao).update(situacao=1)
		return redirect('indexpanicbutton')

def alerta (request, key): 

	try:
		contador = Botao.objects.filter(key_botao= key,situacao = 1).count()


		if contador == 1:
			Botao.objects.filter(key_botao=key).update(situacao=2)
			return HttpResponse (contador)
		else:
			return HttpResponse (contador)

	except ObjectDoesNotExist:
		return HttpResponse ("0")



#def chat(request):
 #   return render(request, 'unlock/chat.html', {})

#def room(request, room_name):
#	return render(request, 'unlock/room.html', {
#		'room_name_json': mark_safe(json.dumps(room_name))
#		})

def aula(request):
	if not request.user.is_authenticated:
		return render(request, 'unlock/entrar.html')
	lista = Lampada.objects.order_by('numero_lampada') #[:5]
	context = {'lista': lista}
	return render(request, 'unlock/aula.html', context)

def ligarlampada(request):
	lampada = request.POST['lampada']
	Lampada.objects.filter(id=lampada).update(status=True)
	return redirect('aula')

def desligarlampada(request):
	lampada = request.POST['lampada']
	Lampada.objects.filter(id=lampada).update(status=False)
	return redirect('aula')