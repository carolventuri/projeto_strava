from django.utils.translation import gettext_lazy as _
from django.db import models

class TipoEsporte(models.TextChoices):
    RUN = "CORRIDA", _("Corrida")
    TRAIL_RUN = "CORRIDA_TRILHAS", _("Corrida de Trilhas")
    BIKE = "TREINO_BICICLETA", _("Treino de Bicicleta")
    WALK = "CAMINHADA", _("Caminhada")
    HIIT = "TREINO_ALTA", _("Treino de Alta Intensidade")
    STRENGTH = "TREINO_FORCA", _("Treino de Força")
    CARDIO = "TREINO_AEROBICO", _("Treino Aerobico")
    SWIMMING = "NATACAO", _("Natação")
