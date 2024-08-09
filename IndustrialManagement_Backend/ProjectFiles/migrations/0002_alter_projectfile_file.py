# Generated by Django 5.0 on 2024-08-09 16:39

import ProjectFiles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectFiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectfile',
            name='file',
            field=models.FileField(upload_to='media/', validators=[ProjectFiles.models.validate_file_extension]),
        ),
    ]
