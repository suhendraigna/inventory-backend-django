from django.urls import path
from .views import BarangMasukView, BarangKeluarView

urlpatterns = [
    path('barang-masuk/', BarangMasukView.as_view()),
    path('barang-keluar/', BarangKeluarView.as_view()),
]