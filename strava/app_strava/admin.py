from django.contrib import admin
from .models import Atividade, Clube, Equipamento, Perfil, Record, DesafioTempo, DesafioAtividades, DesafioTempoAtividades

admin.site.register((Atividade, Clube, Equipamento, Perfil, Record, DesafioTempo, DesafioAtividades, DesafioTempoAtividades))

# Register your models here.
