# Generated by Django 4.1.3 on 2022-11-20 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0013_project_project_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="project_live_link",
            field=models.TextField(blank=True, default="", max_length=500),
        ),
    ]