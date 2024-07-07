# Generated by Django 4.2.2 on 2023-07-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_config_bypass_background_check_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='bypass_corrupted_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='config',
            name='bypass_eye_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='config',
            name='bypass_head_check',
            field=models.BooleanField(default=False),
        ),
    ]
