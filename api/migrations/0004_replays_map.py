# Generated by Django 2.1 on 2018-12-10 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20181209_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='replays',
            name='map',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]