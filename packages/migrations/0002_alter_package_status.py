# Generated by Django 4.2.10 on 2024-04-09 19:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("packages", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="package",
            name="status",
            field=models.CharField(
                choices=[
                    ("NONE", "None"),
                    ("PENDING", "Pending"),
                    ("SUCCESS", "Success"),
                    ("FAILED", "Failed"),
                ],
                max_length=100,
            ),
        ),
    ]