# Generated by Django 3.0 on 2024-04-08 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_aquiz_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aquiz',
            name='user',
        ),
    ]
