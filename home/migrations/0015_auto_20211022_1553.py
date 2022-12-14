# Generated by Django 3.2.4 on 2021-10-22 10:23

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_hsnc_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treatments',
            old_name='title_1',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='hsnc',
            name='para_1',
        ),
        migrations.RemoveField(
            model_name='hsnc',
            name='para_2',
        ),
        migrations.RemoveField(
            model_name='hsnc',
            name='para_3',
        ),
        migrations.RemoveField(
            model_name='hsnc',
            name='title_2',
        ),
        migrations.RemoveField(
            model_name='hsnc',
            name='title_3',
        ),
        migrations.AddField(
            model_name='hsnc',
            name='content',
            field=tinymce.models.HTMLField(default=''),
        ),
    ]
