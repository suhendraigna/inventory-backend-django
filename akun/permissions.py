from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.exceptions import AuthenticationFailed

def ambil_role_dari_token(request):
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        raise AuthenticationFailed("Token tidak ditemukan")

    try:
        token = auth_header.split()[1]
        decoded = AccessToken(token)
        return decoded.get('role')
    except Exception:
        raise AuthenticationFailed("Token tidak valid")
    
class IsAdmin(BasePermission):
    message = "Anda tidak memilik akses"
    
    def has_permission(self, request, view):
        role = ambil_role_dari_token(request)
        return role == "admin"

class IsStaff(BasePermission):
    message = "Anda tidak memiliki aksess"

    def has_permission(self, request, view):
        role = ambil_role_dari_token(request)
        return role == "staff"

class IsAdminOrStaff(BasePermission):
    message = "Anda tidak memiliki akses"
    
    def has_permission(self, request, view):
        role = ambil_role_dari_token(request)
        return role in ["admin", "staff"]