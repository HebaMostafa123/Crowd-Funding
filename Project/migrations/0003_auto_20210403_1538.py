# Generated by Django 3.1.7 on 2021-04-03 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0002_auto_20210403_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproject',
            name='is_cancelled',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
