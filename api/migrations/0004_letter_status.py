# Generated by Django 2.1.5 on 2019-01-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190120_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Sent'), (2, 'Read')], default=0),
        ),
    ]