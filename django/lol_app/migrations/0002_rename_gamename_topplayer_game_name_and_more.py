# Generated by Django 5.0.6 on 2024-08-06 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lol_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topplayer',
            old_name='gameName',
            new_name='game_name',
        ),
        migrations.RenameField(
            model_name='topplayer',
            old_name='tagLine',
            new_name='tag_line',
        ),
    ]
