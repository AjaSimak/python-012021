from django.db import models

class Auto(models.Model):
  registracni_znacka = models.CharField(max_length=30)
  znacka_typ_auta = models.CharField(max_length=30)
  pocet_najetych_km = models.IntegerField()
  datum_posledni_technicke = models.DateField()
  vypujceni_auta = models.ForeignKey("Vypujcka", on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.znacka_typ_auta

class Zakaznik(models.Model):
  jmeno = models.CharField(max_length=30)
  prijmeni = models.CharField(max_length=30)
  ridicak = models.CharField(max_length=30)
  datum_narozeni = models.DateField()
  vypujcka = models.ForeignKey("Vypujcka", on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.prijmeni

class Vypujcka(models.Model):
  datum_zacatek_vypujcky = models.DateField()
  datum_konec_vypujcky = models.DateField()
  cena_vypujcky = models.IntegerField()