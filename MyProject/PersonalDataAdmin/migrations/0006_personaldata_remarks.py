# Generated by Django 4.1.5 on 2023-03-04 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PersonalDataAdmin", "0005_student"),
    ]

    operations = [
        migrations.AddField(
            model_name="personaldata",
            name="remarks",
            field=models.TextField(default=""),
        ),
    ]
