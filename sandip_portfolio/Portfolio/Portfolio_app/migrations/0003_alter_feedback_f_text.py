# Generated by Django 4.1.6 on 2023-02-04 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio_app', '0002_feedback_f_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='F_text',
            field=models.TextField(default=''),
        ),
    ]