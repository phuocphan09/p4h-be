# Generated by Django 4.2 on 2023-05-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('action_log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventlog',
            name='timestamp_server',
            field=models.CharField(default='null', max_length=13),
            preserve_default=False,
        ),
    ]