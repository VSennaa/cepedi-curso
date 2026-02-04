from django.urls import path, include

from . import views

from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.lista_alunos),
    path('novo/', views.cadastrar_aluno),
    path('accounts/', include('django.contrib.auth.urls')),
]
=======
    path('', views.index, name='index'),              # ← ISSO
    path('lista/', views.lista_alunos, name='lista'),
    path('cadastrar/', views.cadastrar_aluno, name='cadastrar'),
]
>>>>>>> voltando
