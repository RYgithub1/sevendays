# Generated by Django 3.2.8 on 2021-11-01 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0005_genericpage_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='iamge',
            new_name='image',
        ),
    ]
