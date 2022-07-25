# Generated by Django 3.1.3 on 2022-07-25 03:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='1', max_length=100)),
                ('Website', models.CharField(default='LinkedIn', max_length=100)),
                ('url', models.CharField(default='www.error.com', max_length=1000)),
                ('Company', models.CharField(default='ApplyAway', max_length=1000)),
                ('Job', models.CharField(default='Error', max_length=1000)),
                ('Description', models.CharField(default='Great Company', max_length=100000)),
                ('Notes', models.CharField(default=' ', max_length=10000)),
                ('Applied', models.CharField(default=' ', max_length=1000)),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
