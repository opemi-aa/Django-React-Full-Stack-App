# Generated by Django 5.2.4 on 2025-07-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_actionlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
