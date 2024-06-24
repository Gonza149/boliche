from django.contrib import admin
from boliche.models import *


class DetalleTragoInline(admin.TabularInline):
    model = DetalleTrago
    extra = 0

# Register your models here.
admin.site.register(Empleado)


@admin.register(Trago)
class TragoAdmin(admin.ModelAdmin):
    inlines = [
        DetalleTragoInline,
    ]
    list_display = (
        'nombre',
        'precio',
    )
    ordering = ['nombre']  # -nombre descendente, nombre ascendente
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )


class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 0


@admin.register(Venta)
class ComprobanteAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    list_per_page = 20
    date_hierarchy = 'fecha'
    list_display = (
        'fecha',
        'barra',
    )

    list_filter = ()

    inlines = [
        DetalleVentaInline]


class DetalleBarraInline(admin.TabularInline):
    model = DetalleBarra
    extra = 0

@admin.register(Barra)
class BarraAdmin(admin.ModelAdmin):
    save_on_top = True
    save_as = True
    list_per_page = 20
    list_display = (
        'nombre',
    )

    list_filter = ()

    inlines = [
        DetalleBarraInline]
