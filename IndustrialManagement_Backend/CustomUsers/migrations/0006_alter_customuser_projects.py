# Generated by Django 5.0 on 2024-10-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUsers', '0005_customuser_projects_and_more'),
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='projects',
            field=models.ManyToManyField(blank=True, to='Projects.project'),
        ),
    ]
