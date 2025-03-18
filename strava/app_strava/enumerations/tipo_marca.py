from django.utils.translation import gettext_lazy as _
from django.db import models

class TipoMarca(models.TextChoices):
    CEM_METROS = "100M", _("100 metros")
    QUATROCENTOS_METROS = "400M", _("400 metros")
    UM_KM = "1KM", _("1 quilômetro")
    CINCO_KM = "5KM", _("5 quilômetros")
    DEZ_KM = "10KM", _("10 quilômetros")
    QUINZE_KM = "15KM", _("15 quilômetros")
    VINTE_KM = "20KM", _("20 quilômetros")
    MEIA = "Meia_Maratona", _("Meia Maratona")
    TRINTA_KM = "30KM", _("30 quilometros")
    MARATONA = "MARATONA", _("Maratona")
    LONGA_DISTANCIA = "MAIOR_DISTANCIA", _("Maior distancia")
    LONGA_DURACAO = "MAIOR_DURACAO", _("Maior duracao")




