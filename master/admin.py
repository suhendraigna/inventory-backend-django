from django.contrib import admin
from .models import Kategori, Supplier, Barang

@admin.register(Barang)
class BarangAdmin(admin.ModelAdmin):
    list_display = ('kode_barang', 'nama_barang', 'stok', 'satuan')
    search_fields = ('kode_barang', 'nama_barang')
    list_filter = ('kategori',)

admin.site.register(Kategori)
admin.site.register(Supplier)