# Generated by Django 4.1.3 on 2022-11-20 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0014_project_project_live_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("company_name", models.CharField(default="", max_length=500)),
                ("company_role", models.CharField(default="", max_length=500)),
                ("company_start_date", models.DateField(default=None)),
                ("company_end_date", models.DateField(blank=True, default=None)),
                (
                    "company_role_description",
                    models.TextField(default="", max_length=5000),
                ),
            ],
        ),
    ]
