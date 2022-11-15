# Generated by Django 4.1.3 on 2022-11-15 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('identificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('mobil', models.CharField(blank=True, max_length=15, null=True)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('especie', models.CharField(blank=True, max_length=30, null=True)),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('edad', models.CharField(max_length=3)),
                ('decendencia', models.BooleanField(blank=True, null=True)),
                ('enfermedades', models.BooleanField(blank=True, null=True)),
                ('cirugias', models.BooleanField(blank=True, null=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RELACION.persona')),
            ],
        ),
    ]
