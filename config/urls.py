from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    
    path('pessoa/', PessoasView.as_view(), name='pessoa'),
    path('ocupacao/', OcupacoesView.as_view(), name='ocupacao'),
    path('instituicao/', InstituicoesView.as_view(), name='instituicao'),
    path('area_saber/', AreasSaberView.as_view(), name='area_saber'),
    path('curso/', CursosView.as_view(), name='curso'),
    path('turma/', TurmasView.as_view(), name='turma'),
    path('disciplina/', DisciplinasView.as_view(), name='disciplina'),
    path('matricula/', MatriculasView.as_view(), name='matricula'),
    path('avaliacao/', AvaliacoesView.as_view(), name='avaliacao'),
    path('frequencia/', FrequenciasView.as_view(), name='frequencia'),
    path('turnos/', TurnosView.as_view(), name='turnos'),
    path('cidade/', CidadesView.as_view(), name='cidade'),
    path('ocorrencia/', OcorrenciasView.as_view(), name='ocorrencia'),
    path('curso_disciplina/', CursoDisciplinasView.as_view(), name='curso_disciplina'),
    path('avaliacao_tipo/', AvaliacaoTiposView.as_view(), name='avaliacao_tipo'),
]
