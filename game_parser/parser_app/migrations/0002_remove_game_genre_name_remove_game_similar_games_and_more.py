# Generated by Django 4.0.3 on 2022-03-11 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='genre_name',
        ),
        migrations.RemoveField(
            model_name='game',
            name='similar_games',
        ),
        migrations.AlterField(
            model_name='game',
            name='summary',
            field=models.CharField(max_length=500),
        ),
    ]
