# Generated by Django 4.0.5 on 2022-07-25 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0006_data_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='Status',
        ),
    ]
