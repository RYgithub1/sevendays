# Generated by Django 3.2.8 on 2021-11-01 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpage',
            name='introduction',
            field=models.TextField(blank=True, null=True),
        ),
    ]