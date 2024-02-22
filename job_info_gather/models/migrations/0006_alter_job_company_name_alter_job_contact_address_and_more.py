# Generated by Django 5.0.1 on 2024-01-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("models", "0005_alter_job_company_name_alter_job_contact_address_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="company_name",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="job",
            name="contact_address",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="job",
            name="contact_name",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_location",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_salary",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="job",
            name="job_title",
            field=models.CharField(max_length=256),
        ),
    ]