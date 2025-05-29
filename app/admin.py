from django.contrib import admin
from .models import (
    Cidade, Ocupacao, Pessoa, InstituicaoEnsino, AreaSaber,
    Curso, Turma, Disciplina, Matricula, Avaliacao, Frequencia,
    Turnos, Ocorrencia, CursoDisciplina, AvaliacaoTipo, PessoaTurma
)

# i) Ocupação e Pessoas
class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]

# ii) Instituição e Cursos
class CursoInlineInstituicao(admin.TabularInline):
    model = Curso
    extra = 1

@admin.register(InstituicaoEnsino)
class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    inlines = [CursoInlineInstituicao]

# iii) Área do saber e Cursos
class CursoInlineArea(admin.TabularInline):
    model = Curso
    extra = 1

@admin.register(AreaSaber)
class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoInlineArea]

# iv) Curso e Disciplinas (via CursoDisciplina)
class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline]

# v) Disciplina e Avaliações
class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

# vi) Turma e Pessoas (via PessoaTurma)
class PessoaTurmaInline(admin.TabularInline):
    model = PessoaTurma
    extra = 1

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    inlines = [PessoaTurmaInline]

# Pessoa (com frequência)
class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = [FrequenciaInline]

# Cidade
@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'uf']

# Registros simples
admin.site.register(Matricula)
admin.site.register(AvaliacaoTipo)
admin.site.register(Ocorrencia)
admin.site.register(Turnos)
admin.site.register(CursoDisciplina)
admin.site.register(PessoaTurma)