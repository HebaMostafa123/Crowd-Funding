# Generated by Django 3.1.7 on 2021-04-03 20:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CrowdUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(blank=True, upload_to='images/user/')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDonation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_body', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('total_target', models.DecimalField(decimal_places=2, max_digits=9)),

                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('is_cancelled', models.BooleanField(default=False, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.category')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projectOwner', to='Project.crowduser')),
                ('user_comment', models.ManyToManyField(related_name='user_comment_join', through='Project.ProjectComment', to='Project.CrowdUser')),
                ('user_donation', models.ManyToManyField(related_name='user_donation_join', through='Project.ProjectDonation', to='Project.CrowdUser')),
                ('user_rate', models.ManyToManyField(related_name='user_rate_join', through='Project.ProjectRate', to='Project.CrowdUser')),
                ('user_report', models.ManyToManyField(related_name='user_report_join', through='Project.ProjectReport', to='Project.CrowdUser')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectTag', to='Project.userproject')),
            ],
        ),
        migrations.AddField(
            model_name='projectreport',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectReported', to='Project.userproject'),
        ),
        migrations.AddField(
            model_name='projectreport',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectReporter', to='Project.crowduser'),
        ),
        migrations.AddField(
            model_name='projectrate',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectRated', to='Project.userproject'),
        ),
        migrations.AddField(
            model_name='projectrate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectRater', to='Project.crowduser'),
        ),
        migrations.CreateModel(
            name='ProjectPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_picture', models.ImageField(blank=True, upload_to='images/project/')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectPictureProject', to='Project.userproject')),
            ],
        ),
        migrations.AddField(
            model_name='projectdonation',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectDonnated', to='Project.userproject'),
        ),
        migrations.AddField(
            model_name='projectdonation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectDonnater', to='Project.crowduser'),
        ),
        migrations.AddField(
            model_name='projectcomment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectCommented', to='Project.userproject'),
        ),
        migrations.AddField(
            model_name='projectcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectCommenter', to='Project.crowduser'),
        ),
        migrations.CreateModel(
            name='FeaturedProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectFeatureProject', to='Project.userproject')),
            ],
        ),
    ]
