# Generated by Django 3.1.7 on 2021-03-15 10:36

import apps.user.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('link', models.URLField(blank=True, verbose_name='link')),
                ('bio', models.TextField(blank=True, verbose_name='bio')),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='d', max_length=1)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['email'], unique=True)),
                ('profile_pic', models.ImageField(blank=True, default='default_prof.png', null=True, upload_to='')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
            ],
            options={
                'verbose_name': 'myuser',
                'verbose_name_plural': 'myusers',
            },
            managers=[
                ('objects', apps.user.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FollowerFollowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accept', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(through='user.FollowerFollowing', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
