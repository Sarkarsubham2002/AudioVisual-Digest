# Generated by Django 4.2.9 on 2024-01-27 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0002_remove_customuser_bio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]