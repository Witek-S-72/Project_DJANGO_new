# Generated by Django 4.1.5 on 2023-03-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PersonalDataAdmin", "0009_alter_student_dekan_remarks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="dekan_remarks",
            field=models.TextField(null=True),
        ),
    ]
