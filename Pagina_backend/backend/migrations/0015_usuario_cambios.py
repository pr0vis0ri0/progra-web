# Generated by Django 4.1.7 on 2023-06-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_usuario_delete_listapropiedades'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cambios',
            field=models.IntegerField(default=0),
        ),
    ]