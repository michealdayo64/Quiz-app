# Generated by Django 4.2.11 on 2024-04-09 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_questions_ans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='ans',
        ),
    ]