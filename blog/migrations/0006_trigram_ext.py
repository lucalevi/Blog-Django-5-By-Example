# Generated by Django 5.0.7 on 2024-08-06 08:23
from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_post_tags"),
    ]

    operations = [TrigramExtension()]
