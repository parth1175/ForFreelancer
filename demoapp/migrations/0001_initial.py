# Generated by Django 4.0.5 on 2022-07-09 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('Salary', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('Distance', models.IntegerField()),
            ],
        ),
    ]
