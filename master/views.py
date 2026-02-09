from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Kategori, Supplier, Barang
from .serializers import KategoriSerializer, SupplierSerializer, BarangSerializer

class KategoriView(APIView):
    def get(self, request):
        data = Kategori.objects.all()
        serializer = KategoriSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KategoriSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "pesan": "Kategori berhasil ditambahkan"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            kategori = Kategori.objects.get(id=id)
        except Kategori.DoesNotExist:
            return Response(
                {
                    "pesan": "Kategori tidak ditemukan"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = KategoriSerializer(kategori, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "pesan": "Kategori berhasil diupdate"
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            kategori = Kategori.objects.get(id=id)
        except Kategori.DoesNotExist:
            return Response(
                {
                    "pesan": "Kategori tidak ditemukan"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        kategori.delete()
        return Response(
            {
                "pesan": "Kategori berhasil dihapus"
            },
            status=status.HTTP_200_OK
        )

class SupplierView(APIView):
    def get(self, request):
        data = Supplier.objects.all()
        serializer = SupplierSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SupplierSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "pesan": "Supplier berhasil ditambahkan"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BarangView(APIView):
    def get(self, request):
        data = Barang.objects.all()
        serializer = BarangSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BarangSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "pesan": "Barang berhasil ditambahkan"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            barang = Barang.objects.get(id=id)
        except Barang.DoesNotExist:
            return Response(
                {
                    "pesan": "Barang tidak ditemukan"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = BarangSerializer(barang, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "pesan": "Barang berhasil diupdate"
                },
                status=status.HTTP_200_OK
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            barang = Barang.objects.get(id=id)
        except Barang.DoesNotExist:
            return Response(
                {
                    "pesan": "Barang tidak ditemukan"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        barang.delete()
        return Response(
            {
                "pesan": "Barang berhasil dihapus"
            },
            status=status.HTTP_200_OK
        )