from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.lista_alunos),
    path('novo/', views.cadastrar_aluno),
    path('accounts/', include('django.contrib.auth.urls')),
]
