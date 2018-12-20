from django.conf.urls import url

from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
#from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
#from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^reset-password/$', password_reset, name='reset_password'),
	url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
	url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
	url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),
#	url(r'^change-password/$', auth_views.PasswordChangeView.as_view()),
	url(r'^$', views.index, name='index'),
	url(r'^erro$', views.erro, name='erro'),
	url(r'^entrar$', views.entrar, name='entrar'),
	url(r'^novo_usuario$', views.novo_usuario, name='novo_usuario'),
	url(r'^novo_usuario_controller$', views.novo_usuario_controller, name='novo_usuario_controller'),
	url(r'^logout_controller$', views.logout_controller, name='logout_controller'),
	url(r'^login_controller$', views.login_controller, name='login_controller'),
	url(r'^meuusuario$', views.meuusuario, name='meuusuario'),
	url(r'^alterar_usuario$', views.alterar_usuario, name='alterar_usuario'),
	url(r'^alterar_usuario_controller$', views.alterar_usuario_controller, name='alterar_usuario_controller'),
	url(r'^porta$', views.porta, name='porta'), # pagina de lista
	url(r'^porta/(?P<porta_id>[0-9]+)/$', views.infoporta, name='infoporta'), #pagina de cada produto
	url(r'^add_porta$', views.add_porta, name='add_porta'), #adicionar porta
	url(r'^add_porta_controller$', views.add_porta_controller, name='add_porta_controller'), #controller
	url(r'^pessoa$', views.pessoa, name='pessoa'), # pagina de lista
	url(r'^pessoa/(?P<pessoas_id>[0-9]+)/$', views.infopessoa, name='infopessoa'), #pagina de cada produto
	url(r'^add_setor$', views.add_setor, name='add_setor'), #adicionar setor
	url(r'^add_setor_controller$', views.add_setor_controller, name='add_setor_controller'), #controller
	url(r'^add_pessoa$', views.add_pessoa, name='add_pessoa'), #adicionar pessoa
	url(r'^add_pessoa_controller$', views.add_pessoa_controller, name='add_pessoa_controller'), #controller
	url(r'^teste$', views.teste, name='teste'),
	url(r'^projetos$', views.projetos, name='projetos'),
	url(r'^add_acesso$', views.add_acesso, name='add_acesso'), #adicionar acesso
	url(r'^add_acesso_controller$', views.add_acesso_controller, name='add_acesso_controller'), #controller
	url(r'^blq_acesso_controller$', views.blq_acesso_controller, name='blq_acesso_controller'), #bloquear acesso
	url(r'^desblq_acesso_controller$', views.desblq_acesso_controller, name='desblq_acesso_controller'), #desbloquear acesso
	url(r'^registro$', views.registro, name='registro'),
	url(r'^relatorio_registro$', views.relatorio_registro, name='relatorio_registro'),
	url(r'^relatorio_registro_pessoa$', views.relatorio_registro_pessoa, name='relatorio_registro_pessoa'),
	url(r'^relatorio_registro_porta$', views.relatorio_registro_porta, name='relatorio_registro_porta'),
	url(r'^acesso_controller/(?P<porta>\w+)/(?P<carteira>\w+)/$', views.acesso_controller, name='acesso_controller'), #controller
	################################
	url(r'^indexpanicbutton$', views.indexpanicbutton, name='indexpanicbutton'),
	url(r'^paginadiego$', views.paginadiego, name='paginadiego'),
	url(r'^indexpanicbutton/(?P<botao_id>[0-9]+)/$', views.infobotao, name='infobotao'), #pagina de cada produto
	url(r'^add_botao$', views.add_botao, name='add_botao'),
	url(r'^add_botao_controller$', views.add_botao_controller, name='add_botao_controller'),
	url(r'^normalizar$', views.normalizar, name='normalizar'),
	url(r'^alerta/(?P<key>\w+)$', views.alerta, name='alerta'),
	url(r'^aula$', views.aula, name='aula'),
	url(r'^ligarlampada$', views.ligarlampada, name='ligarlampada'), #ligar lampada
	url(r'^desligarlampada$', views.desligarlampada, name='desligarlampada'), #desligar lampada
#	url(r'^chat$', views.chat, name='chat'),
#	url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]