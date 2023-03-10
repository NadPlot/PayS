# Generated by Django 4.1.7 on 2023-02-24 13:44

import os

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        DJANGO_SU_NAME = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        DJANGO_SU_EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        superuser = User.objects.create_superuser(
            username=DJANGO_SU_NAME,
            email=DJANGO_SU_EMAIL,
            password=DJANGO_SU_PASSWORD,
            last_login='2023-02-24 13:44',
        )

        superuser.save()

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                (
                    'id', models.CharField(
                        primary_key=True,
                        max_length=50,
                    ),
                ),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RunPython(generate_superuser),
    ]
