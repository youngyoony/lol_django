# Generated by Django 5.0.6 on 2024-08-06 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puuid', models.TextField()),
                ('gameName', models.TextField()),
                ('tagLine', models.TextField()),
            ],
        ),
    ]