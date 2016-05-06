from django.contrib import admin
from somemes.core.models import Meme

# Register your models here.

class MemeModelAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'imagem', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('descricao', 'imagem', 'created_at')
    list_filter = ('descricao',)

admin.site.register(Meme, MemeModelAdmin)