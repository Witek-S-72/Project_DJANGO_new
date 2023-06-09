# Generated by Django 4.1.5 on 2023-03-09 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Notes", "0004_alter_note_create_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("category_name", models.CharField(max_length=50, unique=True)),
            ],
            options={
                "verbose_name": "Kategoria",
                "verbose_name_plural": "Kategorie",
            },
        ),
        migrations.AddField(
            model_name="note",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="Notes.category",
            ),
        ),
    ]
