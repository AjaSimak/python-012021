# Generated by Django 3.2 on 2021-04-24 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registracni_znacka', models.CharField(max_length=30)),
                ('znacka_typ_auta', models.SlugField(max_length=30)),
                ('pocet_najetych_km', models.IntegerField()),
                ('datum_posledni_technicke', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Vypujcka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum_zacatek_vypujcky', models.DateField()),
                ('datum_konec_vypujcky', models.DateField()),
                ('cena_vypujcky', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Zakaznik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=30)),
                ('prijmeni', models.CharField(max_length=30)),
                ('ridicak', models.SlugField()),
                ('datum_narozeni', models.DateField()),
            ],
        ),
    ]
