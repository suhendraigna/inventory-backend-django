import uuid
from django.db import models

class Kategori(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_kategori = models.CharField(max_length=100)
    keterangan = models.TextField(blank=True)

    def __str__(self):
        return self.nama_kategori

class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama_supplier = models.CharField(max_length=150)
    telepon = models.CharField(max_length=30)
    alamat = models.TextField()

    def __str__(self):
        return self.nama_supplier

class Barang(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kode_barang = models.CharField(max_length=50, unique=True)
    nama_barang = models.CharField(max_length=150)

    kategori = models.ForeignKey(
        Kategori,
        on_delete = models.CASCADE
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete = models.CASCADE
    )

    stok = models.IntegerField()
    satuan = models.CharField(max_length=50)

    harga_beli = models.DecimalField(max_digits=12, decimal_places=2)
    harga_jual = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nama_barang