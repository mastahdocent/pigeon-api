# Generated by Django 2.1.5 on 2019-01-26 20:38

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_letter_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.avatars_path),
        ),
    ]