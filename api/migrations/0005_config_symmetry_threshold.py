# Generated by Django 4.2.2 on 2023-07-24 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_config_greyness_threshold'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='symmetry_threshold',
            field=models.FloatField(default=20),
        ),
    ]
