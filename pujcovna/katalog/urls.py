from django.urls import path
from . import views

urlpatterns = [
  path("", views.IndexView.as_view(), name="index"),
  path("seznam", views.SeznamView.as_view(), name="seznam"),
  path("vypujcka_list", views.VypujckaView.as_view(), name="vypujcka_list"),
  path("auto_list", views.AutoView.as_view(), name="auto_list"),
  path("zakaznik_list", views.ZakaznikView.as_view(), name="zakaznik_list")
]

