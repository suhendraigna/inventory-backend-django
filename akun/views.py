from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import AccessToken

from config.response import sukses, gagal
from .models import Pegawai

class LoginView(APIView):
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return gagal("Email dan password harus diisi", 400)

        try:
            pegawai = Pegawai.objects.get(email=email)
        except Pegawai.DoesNotExist:
            return gagal("Email tidak terdaftar", 400)

        if not check_password(password, pegawai.password):
            return gagal("Password salah", 400)

        token = AccessToken()

        token['pegawai_id'] = str(pegawai.id)
        token['nama_lengkap'] = pegawai.nama_lengkap
        token['role'] = pegawai.role

        return sukses("Login berhasil", {
            "access": str(token),
            "nama_lengkap": pegawai.nama_lengkap,
            "role": pegawai.role
        })