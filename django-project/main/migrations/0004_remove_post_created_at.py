# Generated by Django 3.2.15 on 2022-12-17 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20221217_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
    ]
