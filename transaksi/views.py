from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import BarangMasuk, BarangKeluar
from .serializers import BarangMasukSerializer, BarangKeluarSerializer
from master.models import Barang

class BarangMasukView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            barang_id = request.data.get('barang')
            jumlah = int(request.data.get('jumlah'))
        
            barang = get_object_or_404(Barang, id=barang_id)

            stok_lama = barang.stok
            stok_baru = stok_lama + jumlah

            barang.stok = stok_baru
            barang.save()

            serializer = BarangMasukSerializer(data=request.data)
            if serializer.id_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(
                {
                    "pesan": "Barang masuk berhasil, stok bertambah",
                    "stok_sekarang": stok_baru
                },
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {
                    "pesan": "Terjadi kesalahan dalam memproses barang masuk"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        

class BarangKeluarView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        try:
            barang_id = request.data.get('barang')
            jumlah = int(request.data.get('jumlah'))

            barang = get_object_or_404(Barang, id=barang_id)

            stok_lama = barang.stok

            if stok_lama < jumlah:
                return Response(
                    {
                        "pesan": "Stok barang tidak mencukupi"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )             

            stok_baru = stok_lama - jumlah

            barang.stok = stok_baru
            barang.save()

            serializer = BarangKeluarSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(
                {
                    "pesan": "Barang keluar berhasil, stok berkurang",
                    "stok_sekarang": stok_baru
                },
                status=status.HTTP_201_CREATED
            )
        
        except Exception as e:
            return Response(
                {
                    "pesan": "Terjadi kesalahan saat memproses barang keluar"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
