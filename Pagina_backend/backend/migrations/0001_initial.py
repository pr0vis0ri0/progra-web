# Generated by Django 4.1.7 on 2023-07-03 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_comuna', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'MAESTRO_COMUNAS',
                'ordering': ['id_comuna'],
            },
        ),
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id_estado', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_estado', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'MAESTRO_ESTADOS',
                'ordering': ['id_estado'],
            },
        ),
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id_perfil', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_perfil', models.CharField(max_length=75)),
            ],
            options={
                'db_table': 'MAESTRO_PERFILES',
                'ordering': ['id_perfil'],
            },
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id_propiedad', models.AutoField(primary_key=True, serialize=False)),
                ('valor_propiedad', models.IntegerField()),
                ('es_arriendo', models.BooleanField(blank=True, default=0)),
                ('es_venta', models.BooleanField(blank=True, default=0)),
                ('esta_habilitado', models.BooleanField(default=0)),
                ('id_comuna', models.ForeignKey(db_column='id_comuna', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.comuna')),
            ],
            options={
                'db_table': 'MAESTRO_PROPIEDADES',
                'ordering': ['id_propiedad'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_region', models.CharField(max_length=100)),
                ('capital_region', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'MAESTRO_REGIONES',
                'ordering': ['id_region'],
            },
        ),
        migrations.CreateModel(
            name='TipoPropiedad',
            fields=[
                ('id_tipo_propiedad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_propiedad', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'MAESTRO_TIPO_PROPIEDAD',
                'ordering': ['id_tipo_propiedad'],
            },
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id_visita', models.AutoField(primary_key=True, serialize=False)),
                ('dia_visita', models.DateField()),
                ('hora_visita', models.TimeField()),
                ('nombre_completo', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=10)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=11)),
                ('id_propiedad', models.ForeignKey(db_column='id_propiedad', null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.propiedad')),
            ],
            options={
                'db_table': 'MAESTRO_VISITAS',
                'ordering': ['id_visita'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('primer_nombre', models.CharField(default='', max_length=50)),
                ('segundo_nombre', models.CharField(default='', max_length=50)),
                ('apellido_paterno', models.CharField(default='', max_length=50)),
                ('apellido_materno', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('rut', models.CharField(max_length=12)),
                ('fecha_nacimiento', models.DateField(default=None)),
                ('auth_user_id', models.ForeignKey(db_column='auth_user_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'MAESTRO_USUARIOS',
                'ordering': ['id_usuario'],
            },
        ),
        migrations.AddField(
            model_name='propiedad',
            name='id_tipo_propiedad',
            field=models.ForeignKey(db_column='id_tipo_propiedad', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.tipopropiedad'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='id_usuario',
            field=models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.usuario'),
        ),
        migrations.AddField(
            model_name='propiedad',
            name='ultimo_estado',
            field=models.ForeignKey(db_column='ultimo_estado', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.estados'),
        ),
        migrations.CreateModel(
            name='PerfilesUsuario',
            fields=[
                ('id_registro', models.AutoField(primary_key=True, serialize=False)),
                ('id_perfil', models.ForeignKey(db_column='id_perfil', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.perfiles')),
                ('id_usuario', models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.usuario')),
            ],
            options={
                'db_table': 'MAESTRO_ASOC_USUARIO_PERFILES',
                'ordering': ['id_usuario', 'id_perfil'],
            },
        ),
        migrations.AddField(
            model_name='comuna',
            name='id_region',
            field=models.ForeignKey(db_column='id_region', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.region'),
        ),
        migrations.CreateModel(
            name='CaracteristicasPropiedad',
            fields=[
                ('id_carac_prop', models.AutoField(primary_key=True, serialize=False)),
                ('metros_totales', models.IntegerField(default=0)),
                ('metros_utiles', models.IntegerField(default=0)),
                ('cant_dormitorios', models.IntegerField(default=0)),
                ('cant_banos', models.IntegerField(default=0)),
                ('permite_mascotas', models.BooleanField(default=True)),
                ('tiene_bodega', models.BooleanField(default=True)),
                ('tiene_estacionamiento', models.BooleanField(default=True)),
                ('id_propiedad', models.OneToOneField(db_column='id_propiedad', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.propiedad')),
            ],
            options={
                'db_table': 'MAESTRO_ASOC_CARACTERISTICAS_PROPIEDAD',
                'ordering': ['id_propiedad'],
            },
        ),
    ]
