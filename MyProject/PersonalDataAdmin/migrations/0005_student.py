# Generated by Django 4.1.5 on 2023-03-04 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("PersonalDataAdmin", "0004_alter_personaldata_date_of_birth"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("index_numb", models.PositiveIntegerField(unique=True)),
                ("immatr_date", models.DateTimeField()),
                (
                    "person_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="PersonalDataAdmin.personaldata",
                    ),
                ),
            ],
            options={
                "verbose_name": "Student",
                "verbose_name_plural": "Studenci",
            },
        ),
    ]
