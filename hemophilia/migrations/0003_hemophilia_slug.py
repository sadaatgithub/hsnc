# Generated by Django 3.2.4 on 2021-06-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hemophilia', '0002_auto_20210618_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='hemophilia',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
