# Generated by Django 3.1.4 on 2020-12-04 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('os_api', '0009_auto_20201205_0224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permiss',
            name='live_time',
        ),
        migrations.AddField(
            model_name='permiss',
            name='live_time',
            field=models.DurationField(verbose_name='Время жизни'),
        ),
    ]
