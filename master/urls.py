from django.urls import path
from .views import KategoriView, SupplierView, BarangView

urlpatterns = [
    path('kategori/', KategoriView.as_view()),
    path('kategori/<uuid:id>/', KategoriView.as_view()),

    path('supplier/', SupplierView.as_view()),

    path('barang/', BarangView.as_view()),
    path('barang/<uuid:id>/', BarangView.as_view()),
]