# Generated by Django 5.0 on 2024-10-18 13:48

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('social_id_number', models.CharField(blank=True, max_length=30)),
                ('personal_id_number', models.CharField(blank=True, max_length=30)),
                ('mobile_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('phone_number', models.CharField(blank=True, max_length=30)),
                ('education_level', models.CharField(choices=[('BSc', 'BSc'), ('Ms', 'Ms'), ('PhD', 'PhD'), ('Prof', 'Prof')], max_length=20)),
                ('admin', models.BooleanField(default=False)),
                ('crud_project', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'Custom User',
                'verbose_name_plural': 'Custom Users',
            },
        ),
    ]
