# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 04:42
from __future__ import unicode_literals

import designer.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('designer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=10)),
                ('long_name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=120, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=designer.models.profile_media_upload_location)),
                ('website', models.URLField(blank=True, max_length=50, null=True)),
                ('data', models.IntegerField(default=0)),
                ('data_cap', models.IntegerField(default=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('public', models.BooleanField(default=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=designer.models.repo_media_upload_location)),
                ('created_at', models.DateTimeField()),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('head_sha1', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='team',
        ),
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
        migrations.RemoveField(
            model_name='team',
            name='leader',
        ),
        migrations.RemoveField(
            model_name='team',
            name='plan',
        ),
        migrations.CreateModel(
            name='TeamProfile',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='designer.Profile')),
                ('public', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField()),
                ('last_updated', models.DateTimeField()),
                ('members', models.ManyToManyField(related_name='team_members', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('designer.profile',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='designer.Profile')),
                ('public_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            bases=('designer.profile',),
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='designer.Profile'),
        ),
        migrations.AddField(
            model_name='project',
            name='license',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='designer.License'),
        ),
        migrations.AddField(
            model_name='project',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_repo_in_repo', to='designer.Project'),
        ),
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ManyToManyField(blank=True, related_name='team', to='designer.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='designer.Plan'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='team_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_profile', to='designer.TeamProfile'),
        ),
    ]
