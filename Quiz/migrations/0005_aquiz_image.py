# Generated by Django 4.2.11 on 2024-04-08 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0004_alter_aquiz_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='aquiz',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='quiz'),
        ),
    ]
