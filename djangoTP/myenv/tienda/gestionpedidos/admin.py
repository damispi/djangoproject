from django.contrib import admin

from gestionpedidos.models import clientes,articulos, pedidos
class clientesadmin(admin.ModelAdmin):
    list_display=('nombre','direccion','telefono')
    search_fields=("nombre","telefono")


admin.site.register(clientes,clientesadmin )
admin.site.register(articulos)
admin.site.register(pedidos)