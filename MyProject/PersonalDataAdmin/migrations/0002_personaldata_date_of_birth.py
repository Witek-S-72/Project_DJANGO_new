# Generated by Django 4.1.5 on 2023-03-03 17:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("PersonalDataAdmin", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="personaldata",
            name="date_of_birth",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
