# Generated by Django 4.1.7 on 2023-05-17 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_rename_id_departamento_visita_id_propiedad'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='id_comuna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.comuna'),
        ),
    ]
