from rest_framework import serializers
from .models import BarangMasuk, BarangKeluar

class BarangMasukSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarangMasuk
        fields = '__all__'
        read_only_fields = ['tanggal_masuk']

class BarangKeluarSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarangKeluar
        fields = '__all__'
        read_only_fields = ['tanggal_keluar']