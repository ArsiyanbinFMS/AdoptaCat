# Generated by Django 2.2 on 2020-04-28 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0002_auto_20200427_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
    ]
