from django.urls import path
from .views import alterar_diario, criar_diarios, criar_usuario, excluir_diario, fazer_login, fazer_logout, informacoes_usuario, listar_diario

urlpatterns = [
    path('login', fazer_login, name='login'),
    path('diary_list', listar_diario, name='list'),
    path('logout', fazer_logout, name='logout'),
    path('create_diary', criar_diarios, name='create'),
    path('delete_diary/<id>/', excluir_diario, name='delete'),
    path('update_diary/<id>/', alterar_diario, name='update'),
    path('user_info', informacoes_usuario, name='info'),
    path('create_user', criar_usuario, name="create_user")
]