# Generated by Django 3.1.7 on 2021-04-09 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcomment',
            name='comment_body',
            field=models.TextField(max_length=100),
        ),
    ]
