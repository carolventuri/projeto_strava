from ..models import Desafio
from django.db import models

class DesafioAtividades(Desafio):
    meta_atividades = models.IntegerField(
        null=False, blank=False,
        help_text="Digite a quantidade de atividades da meta",
        verbose_name="Meta de atividades:",
    )

    def __str__(self):
        return f'{self.nome} -(numero) {self.meta_atividades}'
