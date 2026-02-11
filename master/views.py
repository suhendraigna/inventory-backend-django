from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from config.response import sukses, gagal
from akun.permissions import IsAdmin
from .models import Kategori, Supplier, Barang
from .serializers import KategoriSerializer, SupplierSerializer, BarangSerializer

class KategoriView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        data = Kategori.objects.all()
        serializer = KategoriSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KategoriSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return sukses("Kategori berhasil ditambahkan")

        return gagal("Data kategori tidak valid", 400)

    def put(self, request, id):
        try:
            kategori = Kategori.objects.get(id=id)
        except Kategori.DoesNotExist:
            return gagal("Kategori tidak ditemukan", 404)
        
        serializer = KategoriSerializer(kategori, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return sukses("Kategori berhasil diupdate")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            kategori = Kategori.objects.get(id=id)
        except Kategori.DoesNotExist:
            return gagal("Kategori tidak ditemukan", 404)
        
        kategori.delete()
        return sukses("Kategori berhasil dihapus")

class SupplierView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        data = Supplier.objects.all()
        serializer = SupplierSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SupplierSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return sukses("Supplier berhasil ditambahkan")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BarangView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        data = Barang.objects.all()
        serializer = BarangSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BarangSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return sukses("Barang berhasil ditambahkan")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            barang = Barang.objects.get(id=id)
        except Barang.DoesNotExist:
            return gagal("Barang tidak ditemukan", 404)
        
        serializer = BarangSerializer(barang, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return sukses("Barang berhasil diupdate")
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            barang = Barang.objects.get(id=id)
        except Barang.DoesNotExist:
            return gagal("Barang tidak ditemukan", 404)
        
        barang.delete()
        return sukses("Barang berhasil dihapus")