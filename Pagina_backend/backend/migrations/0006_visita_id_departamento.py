# Generated by Django 4.1.7 on 2023-05-17 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_region_capital_region_alter_region_nombre_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='visita',
            name='id_departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.propiedad'),
        ),
    ]
