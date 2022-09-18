# Generated by Django 3.2.4 on 2021-10-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_posts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='posts',
            new_name='content',
        ),
        migrations.AddField(
            model_name='posts',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]