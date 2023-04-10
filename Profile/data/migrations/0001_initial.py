# Generated by Django 4.1.3 on 2022-11-14 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Certification",
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
                ("certification_name", models.CharField(max_length=100)),
                ("certification_publication", models.CharField(max_length=500)),
                ("certification_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Education",
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
                ("education_college", models.CharField(max_length=500)),
                ("education_degree", models.CharField(max_length=500)),
                ("education_gpa", models.FloatField()),
                ("education_start", models.IntegerField(max_length=50)),
                ("education_end", models.IntegerField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("project_name", models.CharField(max_length=500)),
                ("project_description", models.TextField(max_length=1000)),
                ("project_technologies", models.TextField(max_length=500)),
                ("project_link", models.TextField(max_length=500)),
            ],
        ),
    ]