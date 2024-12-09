# Generated by Django 5.1 on 2024-09-04 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_alter_players_p_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='technicalteam',
            name='t_team',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='teams.teams', verbose_name='Equipo al cual pertenece el ET'),
            preserve_default=False,
        ),
    ]
