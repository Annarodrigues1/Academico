from django.contrib import admin
from .models import (
    Cidade, Ocupacao, Pessoa, InstituicaoEnsino, AreaSaber,
    Curso, Turma, Disciplina, Matricula, Avaliacao, Frequencia,
    Turnos, Ocorrencia, CursoDisciplina, AvaliacaoTipo, PessoaTurma
)

# ===== INLINES =====

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class PessoaTurmaInline(admin.TabularInline):
    model = PessoaTurma
    extra = 1

class MatriculaInline(admin.TabularInline):
    model = Matricula
    extra = 1

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class OcorrenciaInline(admin.TabularInline):
    model = Ocorrencia
    extra = 1

class InstituicaoEnsinoInline(admin.TabularInline):
    model = InstituicaoEnsino
    extra = 1

# ===== ADMIN PRINCIPAL =====

@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]

@admin.register(InstituicaoEnsino)
class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

@admin.register(AreaSaber)
class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoInline]

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline]

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    inlines = [PessoaTurmaInline]

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = [MatriculaInline, FrequenciaInline, OcorrenciaInline]

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'uf']
    inlines = [InstituicaoEnsinoInline]

@admin.register(AvaliacaoTipo)
class AvaliacaoTipoAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'curso', 'instituicao', 'data_inicio', 'data_previsao_termino']
    list_filter = ['curso', 'instituicao']
    search_fields = ['pessoa__nome', 'curso__nome']

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'curso', 'disciplina', 'tipo']

@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'curso', 'disciplina', 'numero_faltas']

@admin.register(Ocorrencia)
class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'data', 'pessoa', 'curso', 'disciplina']

@admin.register(Turnos)
class TurnosAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(CursoDisciplina)
class CursoDisciplinaAdmin(admin.ModelAdmin):
    list_display = ['disciplina', 'curso']

@admin.register(PessoaTurma)
class PessoaTurmaAdmin(admin.ModelAdmin):
    list_display = ['pessoa', 'turma']