# Generated by Django 5.0 on 2024-10-18 13:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=30)),
                ('postal_code', models.CharField(blank=True, max_length=30)),
                ('address', models.TextField(max_length=500)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
