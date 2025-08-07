from django.contrib import admin
from apps.suntrack.models import Servicos

class ListandoServicos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'publicada')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Servicos, ListandoServicos)
