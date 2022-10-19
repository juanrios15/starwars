# Generated by Django 4.1.2 on 2022-10-19 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('actor_nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('1', 'Femenino'), ('2', 'Masculino'), ('3', 'Ninguno')], max_length=1, null=True)),
                ('raza', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='personajes.raza')),
            ],
        ),
    ]