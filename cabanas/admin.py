from django.contrib import admin
from .models import Cabana, Promocion, Opinion

@admin.register(Cabana)
class CabanaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'clave', 'costo_por_dia', 'num_personas', 'num_camas')
    search_fields = ('nombre', 'clave')
    list_filter = ('num_personas', 'num_camas')
    # Personalizar título
    admin.site.site_header = "Réntame Admin"
    admin.site.site_title = "Réntame Admin Portal"
    admin.site.index_title = "Administración de Réntame"


@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):
    list_display = ('cabana', 'fecha_inicio', 'fecha_fin')
    list_filter = ('fecha_inicio', 'fecha_fin')
    search_fields = ('cabana__nombre',)


@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cabana', 'fecha')
    search_fields = ('usuario', 'cabana__nombre')
    list_filter = ('fecha',)
