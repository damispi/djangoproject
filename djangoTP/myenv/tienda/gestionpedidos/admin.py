from django.contrib import admin

from gestionpedidos.models import clientes,articulos, pedidos
class clientesadmin(admin.ModelAdmin):
    list_display=('nombre','direccion','telefono')
    search_fields=("nombre","telefono")

class articulosadmin(admin.ModelAdmin):
    list_filter=("seccion",)

class pedidosadmin(admin.ModelAdmin):
    list_display=('numero','fecha','entregado')
    list_filter=('fecha',)
    date_hierarchy='fecha'

admin.site.register(clientes,clientesadmin )
admin.site.register(articulos, articulosadmin)
admin.site.register(pedidos, pedidosadmin)