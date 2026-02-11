from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import AccessToken

from .models import Pegawai

class LoginView(APIView):
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {
                    "pesan": "Email dan password harus diisi"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            pegawai = Pegawai.objects.get(email=email)
        except Pegawai.DoesNotExist:
            return Response(
                {
                    "pesan": "Email tidak terdaftar"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if not check_password(password, pegawai.password):
            return Response(
                {
                    "pesan": "Password salah"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        token = AccessToken()

        token['pegawai_id'] = str(pegawai.id)
        token['nama_lengkap'] = pegawai.nama_lengkap
        token['role'] = pegawai.role

        return Response({
            "access": str(token),
            "nama_lengkap": pegawai.nama_lengkap,
            "role": pegawai.role
        }, status=status.HTTP_200_OK)