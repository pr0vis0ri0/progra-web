# Generated by Django 4.1.7 on 2023-05-17 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_visita_id_departamento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visita',
            old_name='id_departamento',
            new_name='id_propiedad',
        ),
    ]