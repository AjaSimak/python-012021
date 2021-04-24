from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from . import models


class IndexView(View):
  def get(self, request):
    return HttpResponse("Zde bude titulní stránka.")

class SeznamView(View):
  def get(self, request):
    return HttpResponse("Zde bude seznam aut.")

class VypujckaView(ListView):
  model = models.Vypujcka
  template_name = "vypujcka_list.html"

class AutoView(ListView):
  model = models.Auto
  template_name = "auto_list.html"

class ZakaznikView(ListView):
  model = models.Zakaznik
  template_name = "zakaznik_list.html"