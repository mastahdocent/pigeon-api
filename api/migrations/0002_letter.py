# Generated by Django 2.1.5 on 2019-01-19 22:18

import api.letters.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('sent_on', models.DateTimeField(blank=True, null=True)),
                ('read_on', models.DateTimeField(blank=True, null=True)),
                ('recipient_deleted', models.BooleanField(blank=True, default=False)),
                ('recipient_deleted_on', models.DateTimeField(blank=True, null=True)),
                ('sender_deleted', models.BooleanField(blank=True, default=False)),
                ('sender_deleted_on', models.DateTimeField(blank=True, null=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
