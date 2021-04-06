# Generated by Django 3.1.7 on 2021-04-03 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Project', '0005_merge_20210403_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectCommenter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projectdonation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectDonnater', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projectrate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectRater', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projectreport',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectReporter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userproject',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='userproject',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projectOwner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userproject',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='userproject',
            name='user_comment',
            field=models.ManyToManyField(related_name='user_comment_join', through='Project.ProjectComment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userproject',
            name='user_donation',
            field=models.ManyToManyField(related_name='user_donation_join', through='Project.ProjectDonation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userproject',
            name='user_rate',
            field=models.ManyToManyField(related_name='user_rate_join', through='Project.ProjectRate', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userproject',
            name='user_report',
            field=models.ManyToManyField(related_name='user_report_join', through='Project.ProjectReport', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CrowdUser',
        ),
    ]