# Generated by Django 2.1.3 on 2018-11-26 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venvapp', '0003_auto_20181123_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fangse',
            fields=[
                ('symble', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('rela_weight', models.TextField(blank=True, null=True)),
                ('ch_body', models.TextField(blank=True, null=True)),
                ('energy', models.TextField(blank=True, null=True)),
                ('mo_body', models.TextField(blank=True, null=True)),
                ('half_t', models.TextField(blank=True, db_column='half_T', null=True)),
            ],
            options={
                'db_table': 'Fangse',
                'managed': False,
            },
        ),
    ]
