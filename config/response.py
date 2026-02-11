from rest_framework.response import Response

def sukses(pesan, data=None):
    return Response({
        "status": True,
        "pesan": pesan,
        "data": data or {}
    })

def gagal(pesan, status_code=400):
    return Response({
        "status": False,
        "pesan": pesan,
        "data": {}
    }, status=status_code)