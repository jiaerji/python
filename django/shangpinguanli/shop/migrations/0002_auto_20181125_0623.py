# Generated by Django 2.1.3 on 2018-11-24 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='market',
            old_name='object',
            new_name='object1',
        ),
    ]