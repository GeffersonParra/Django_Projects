# Generated by Django 5.1 on 2024-09-03 22:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=30, verbose_name='Posición de juego')),
                ('position_description', models.TextField(max_length=512, verbose_name='Descripción de la posición de juego')),
                ('position_image', models.ImageField(upload_to='photos/positions')),
            ],
            options={
                'verbose_name': 'Posición de juego',
                'verbose_name_plural': 'Posiciones de juego',
                'db_table': 'positions',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=20, verbose_name='Nombre del Equipo')),
                ('flag', models.ImageField(upload_to='photos/teams/flags', verbose_name='Bandera del Equipo')),
                ('shield', models.ImageField(upload_to='photos/teams/shields', verbose_name='Escudo del Equipo')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
                'db_table': 'teams',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TechnicalTeamRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=30, verbose_name='Nombre del rol')),
                ('role_description', models.TextField(max_length=255, verbose_name='Descripción del rol')),
            ],
            options={
                'verbose_name': 'Rol del ET',
                'verbose_name_plural': 'Roles del ET',
                'db_table': 'technicalteamroles',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_first_name', models.CharField(max_length=25, verbose_name='Primer nombre del jugador')),
                ('p_second_name', models.CharField(max_length=25, null=True, verbose_name='Segundo nombre del jugador')),
                ('p_first_last_name', models.CharField(max_length=25, verbose_name='Primer apellido del jugador')),
                ('p_second_last_name', models.CharField(max_length=25, null=True, verbose_name='Segundo apellido del jugador')),
                ('p_photo', models.ImageField(null=True, upload_to='photos/players', verbose_name='Foto del jugador')),
                ('p_birth', models.DateField(null=True, verbose_name='Fecha de nacimiento del jugador')),
                ('p_number', models.PositiveIntegerField(max_length=3, verbose_name='Número de la camiseta del jugador')),
                ('p_is_titular', models.BooleanField(verbose_name='Es jugador titular')),
                ('p_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.playposition', verbose_name='Posición de juego del jugador')),
                ('p_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.teams', verbose_name='Equipo del jugador')),
            ],
            options={
                'verbose_name': 'Jugador',
                'verbose_name_plural': 'Jugadores',
                'db_table': 'players',
                'ordering': ['p_team'],
            },
        ),
        migrations.CreateModel(
            name='TechnicalTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_first_name', models.CharField(max_length=25, verbose_name='Primer nombre del integrante del ET')),
                ('t_second_name', models.CharField(max_length=25, null=True, verbose_name='Segundo nombre del integrante del ET')),
                ('t_first_last_name', models.CharField(max_length=25, verbose_name='Primer apellido del integrante del ET')),
                ('t_second_last_name', models.CharField(max_length=25, null=True, verbose_name='Segundo apellido del integrante del ET')),
                ('t_nationality', models.CharField(max_length=30, verbose_name='Nacionalidad')),
                ('t_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.technicalteamroles', verbose_name='Rol del integrante del ET')),
            ],
            options={
                'verbose_name': 'ET',
                'verbose_name_plural': 'ET',
                'db_table': 'technicalteam',
                'ordering': ['id'],
            },
        ),
    ]
