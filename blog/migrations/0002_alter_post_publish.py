# Generated by Django 5.0.7 on 2024-08-01 08:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="publish",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
