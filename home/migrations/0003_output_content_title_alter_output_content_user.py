# Generated by Django 4.2.9 on 2024-01-27 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_output_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='output_content',
            name='title',
            field=models.CharField(default='Your Default Value', max_length=255),
        ),
        migrations.AlterField(
            model_name='output_content',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
