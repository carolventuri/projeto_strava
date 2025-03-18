from django.utils.translation import gettext_lazy as _
from django.db import models

class Genero(models.TextChoices):
    MAN = "HOMEM", _("Homem")
    WOMAN = "MULHER", _("Mulher")
    NON_BINARY = "NAO_BINARIO", _("Nao binario")
    NOT_INFORMED = "NAO_INFORMADO", _("Nao informado")
