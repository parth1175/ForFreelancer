# Generated by Django 4.0.5 on 2022-08-02 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0013_alter_data_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Applied',
            field=models.CharField(default='Missing', max_length=1000),
        ),
        migrations.AlterField(
            model_name='data',
            name='Company',
            field=models.CharField(default='Missing', max_length=1000),
        ),
        migrations.AlterField(
            model_name='data',
            name='Description',
            field=models.CharField(default='Missing', max_length=100000),
        ),
        migrations.AlterField(
            model_name='data',
            name='Job',
            field=models.CharField(default='Missing', max_length=1000),
        ),
        migrations.AlterField(
            model_name='data',
            name='Url',
            field=models.CharField(default='Missing', max_length=1000),
        ),
        migrations.AlterField(
            model_name='data',
            name='Website',
            field=models.CharField(default='Missing', max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='user',
            field=models.CharField(default='Missing', max_length=100),
        ),
    ]
