from django.contrib import admin
from .models import Atividade, Clube, Equipamento, Perfil, Record, DesafioTempo

admin.site.register((Atividade, Clube, Equipamento, Perfil, Record, DesafioTempo))

# Register your models here.
