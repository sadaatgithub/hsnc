# Generated by Django 3.2.4 on 2021-06-22 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vWd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(max_length=100)),
                ('para_1', models.TextField(blank=True, null=True)),
                ('title_2', models.CharField(blank=True, max_length=100)),
                ('para_2', models.TextField(blank=True, null=True)),
                ('title_3', models.CharField(blank=True, max_length=100)),
                ('para_3', models.TextField(blank=True, null=True)),
                ('title_4', models.CharField(blank=True, max_length=100)),
                ('para_4', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(default='')),
            ],
            options={
                'verbose_name_plural': 'von Willebrand Disease',
            },
        ),
    ]