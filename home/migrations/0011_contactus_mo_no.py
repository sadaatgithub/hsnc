# Generated by Django 3.2.4 on 2021-06-23 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210623_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='mo_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
