from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length = 20, null=True, blank=True)

class TodoList(models.Model):
    tarefa = models.CharField(max_length = 20)
    choices_status = [
        ('Pronto', 'Pronto'),
        ('Em andamento', 'Em andamento'),
        ('Pendente', 'Pendente'),
    ]
    status = models.CharField(choices = choices_status, max_length = 12)
    pessoa = models.ForeignKey(
        Pessoa,
        max_length = 20,
        on_delete = models.CASCADE,
        null=True,
        blank=True
    )