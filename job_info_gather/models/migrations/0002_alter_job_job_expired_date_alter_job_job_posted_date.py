# Generated by Django 5.0.1 on 2024-01-25 14:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("models", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="job_expired_date",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_posted_date",
            field=models.TextField(),
        ),
    ]
