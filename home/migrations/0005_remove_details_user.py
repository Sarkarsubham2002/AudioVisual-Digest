# Generated by Django 5.0.1 on 2024-01-28 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_details_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='user',
        ),
    ]
