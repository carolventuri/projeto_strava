from django.utils.translation import gettext_lazy as _
from django.db import models

class Genero(models.TextChoices):
    SNEAKER = "TENIS", _("Tenis")
    BIKE = "BICICLETA", _("Bicicleta")
    SMART_DEVICE = "DISPOSITIVO_INTELIGENTE", _("Dispositivo Inteligente")
