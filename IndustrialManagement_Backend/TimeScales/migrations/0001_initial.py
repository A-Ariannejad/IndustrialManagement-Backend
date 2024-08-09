# Generated by Django 5.0 on 2024-08-09 13:48

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Projects', '0002_alter_project_external_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeScale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_progress_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('time_program_progress_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('date', models.DateTimeField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.project')),
            ],
        ),
    ]
