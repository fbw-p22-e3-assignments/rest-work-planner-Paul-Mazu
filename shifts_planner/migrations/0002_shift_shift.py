# Generated by Django 4.2.1 on 2023-05-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shifts_planner", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="shift",
            name="shift",
            field=models.CharField(
                blank=True,
                choices=[
                    ("00:00 - 08:00", "I shift"),
                    ("08:00 - 16:00", "II shift"),
                    ("16:00 - 00:00", "III shift"),
                ],
                max_length=200,
            ),
        ),
    ]
