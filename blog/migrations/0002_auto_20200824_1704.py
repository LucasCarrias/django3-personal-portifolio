# Generated by Django 3.1 on 2020-08-24 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='descriptiom',
            new_name='description',
        ),
    ]