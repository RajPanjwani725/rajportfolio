# Generated by Django 4.1.3 on 2022-11-19 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "data",
            "0012_rename_project_uupload_to_youtube_project_project_upload_to_youtube",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="project_image",
            field=models.ImageField(
                blank=True, default="", upload_to="static/assets/uploads"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="project_link_linkedin",
            field=models.TextField(blank=True, default="", max_length=500),
        ),
        migrations.AlterField(
            model_name="project",
            name="project_link_youtube",
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
