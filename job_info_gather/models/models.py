from django.db import models

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=256, null=True)
    job_title = models.CharField(max_length=256)
    job_location = models.CharField(max_length=256, null=True)
    job_salary = models.CharField(max_length=256, null=True)
    job_description = models.TextField(null=True)
    job_requirement = models.TextField(null=True)
    job_posted_date = models.TextField()
    job_expired_date = models.TextField(null=True)
    contact_name = models.CharField(max_length=256, null=True)
    contact_phone = models.CharField(max_length=32, null=True)
    contact_address = models.CharField(max_length=256, null=True)
    source_link = models.TextField()
    encode_content_hash = models.CharField(null=True, db_index=True, max_length=64)

    class Meta:
        db_table = "job"

class Website(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    url = models.TextField()
    selector = models.TextField()
    info_url_selector = models.TextField()
    show_more_mode = models.CharField(max_length=32, default="page")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "website"

    class Constants:
        SHOW_MORE_PAGE = "page"
        SHOW_MORE_SCROLL = "scroll"
    
    
    