# Generated by Django 5.0 on 2024-08-09 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('is_controller', models.BooleanField(default=False)),
                ('is_viewer', models.BooleanField(default=False)),
                ('is_calculator', models.BooleanField(default=False)),
                ('is_supporter', models.BooleanField(default=False)),
            ],
        ),
    ]
