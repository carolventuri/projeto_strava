from ..models import Desafio
from django.db import models

class DesafioTempoAtividades(Desafio):
    meta_duracao = models.TimeField(
        null=False, blank=False,
        help_text="Digite a meta",
        verbose_name="Meta de tempo",
    )
    meta_atividades = models.IntegerField(
        null=False, blank=False,
        help_text="Digite a quantidade de atividades da meta",
        verbose_name="Meta de atividades:",
    )

    def __str__(self):
        return f'{self.nome} -(tempo) {self.meta_duracao}-(numero) {self.meta_atividades}'