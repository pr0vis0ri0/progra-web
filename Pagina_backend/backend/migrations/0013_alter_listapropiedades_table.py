# Generated by Django 4.1.7 on 2023-06-10 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_listapropiedades'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='listapropiedades',
            table='vista_detalle_propiedad',
        ),
    ]