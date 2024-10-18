# Generated by Django 5.0 on 2024-10-18 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUsers', '0003_remove_customuser_suborganizations_and_more'),
        ('SubOrganizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='subOrganizations',
            field=models.ManyToManyField(to='SubOrganizations.suborganization'),
        ),
    ]