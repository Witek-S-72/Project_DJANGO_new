# Generated by Django 4.1.5 on 2023-03-07 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Notes", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="note",
            name="author",
        ),
    ]
