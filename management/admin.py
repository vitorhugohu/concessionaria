from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    # Colunas que serão exibidas na listagem da tabela no Admin
    list_display = (
        'id',
        'make',
        'model',
        'price',
        'year_of_manufacture',
        'color',
        'imported',
    )

    # Campos que se tornam links para clicar e editar o registro
    list_display_links = ('id', 'make', 'model')

    # Campo de pesquisa rápida (busca por marca, modelo ou cor)
    search_fields = ('make', 'model', 'color')

    # Filtros laterais para facilitar a navegação
    list_filter = ('imported', 'make', 'year_of_manufacture')

    # Quantidade de itens exibidos por página
    list_per_page = 20