# Generated by Django 3.1.6 on 2021-06-11 12:04

from django.db import migrations, models
import enum


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hsnc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(max_length=100)),
                ('para_1', models.TextField(max_length=enum.auto, null=True)),
                ('title_2', models.CharField(max_length=100)),
                ('para_2', models.TextField(max_length=enum.auto, null=True)),
                ('title_3', models.CharField(max_length=100)),
                ('para_3', models.TextField(max_length=enum.auto, null=True)),
            ],
            options={
                'verbose_name_plural': 'HSNC _Data',
            },
        ),
    ]
