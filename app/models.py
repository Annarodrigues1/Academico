from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} - {self.uf}"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    pai = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nasc = models.DateField()
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    area = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, null=True, blank=True)
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    area = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome

class CursoDisciplina(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.disciplina} - {self.curso}'

class Turma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class PessoaTurma(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pessoa} - {self.turma}'

class Matricula(models.Model):
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

    def __str__(self):
        return f'{self.pessoa} - {self.curso}'

class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    numero_faltas = models.IntegerField()

    def __str__(self):
        return f"{self.pessoa} - {self.disciplina}"

class Turnos(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=200)
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao
