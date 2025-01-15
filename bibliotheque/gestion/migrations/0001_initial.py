# Generated by Django 5.1.5 on 2025-01-15 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
                ('cout', models.DecimalField(decimal_places=2, max_digits=10)),
                ('max_livres', models.IntegerField()),
                ('max_jours', models.IntegerField()),
                ('duree', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('auteur', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exemplaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('disponible', models.BooleanField(default=True)),
                ('livre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.livre')),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=20)),
                ('actif', models.BooleanField(default=True)),
                ('date_inscription', models.DateField(auto_now_add=True)),
                ('date_expiration', models.DateField(blank=True, null=True)),
                ('abonnement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.abonnement')),
            ],
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emprunt', models.DateField(auto_now_add=True)),
                ('date_retour', models.DateField(blank=True, null=True)),
                ('exemplaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.exemplaire')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.membre')),
            ],
        ),
    ]
