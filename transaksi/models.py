import uuid
from django.db import models
from master.models import Barang

class BarangMasuk(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    barang = models.ForeignKey(
        Barang,
        on_delete=models.CASCADE
    )

    jumlah = models.IntegerField()
    tanggal_masuk = models.DateTimeField(auto_now_add=True)
    keterangan = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Masuk - {self.barang.nama_barang}"

class BarangKeluar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    barang = models.ForeignKey(
        Barang,
        on_delete=models.CASCADE
    )

    jumlah = models.IntegerField()
    tanggal_keluar = models.DateTimeField(auto_now_add=True)
    keterangan = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Keluar - {self.barang.nama_barang}"