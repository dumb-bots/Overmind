# Generated by Django 2.1 on 2019-02-05 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_replays_map'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('load', models.IntegerField(default=1)),
                ('player', models.CharField(blank=True, max_length=200, null=True)),
                ('oponent', models.CharField(blank=True, max_length=200, null=True)),
                ('map', models.CharField(blank=True, max_length=200, null=True)),
                ('is_enabled', models.BooleanField(default=True)),
                ('difficulty_player', models.CharField(blank=True, max_length=200, null=True)),
                ('difficulty_opponent', models.CharField(blank=True, max_length=200, null=True)),
                ('bot_player', models.CharField(blank=True, max_length=200, null=True)),
                ('bot_oponent', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
