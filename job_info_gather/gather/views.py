from django.shortcuts import render
import config.config as config
from models.models import Job
from helper.helper import SeleniumCrawler
from helper.extract import constant_extract, geturl
from hashlib import sha224
# Create your views here.
def index(request):
    return render(request, "index.html")

def crawl(request):
    crawler = SeleniumCrawler()
    info_blocks = crawler.crawl(geturl(config.Carelink_url, 1), config.selector_info_url)
    hrefs = [info_block.get_attribute("href") for info_block in info_blocks]
    for href in hrefs:
        crawler.driver.get(href)
        all_content = constant_extract(crawler, config.Carelink_HTML_structure, "all_content")
        if Job.objects.filter(encode_content_hash=sha224(all_content.encode()).hexdigest()).exists():
            continue
        company_name = constant_extract(crawler, config.Carelink_HTML_structure, "company_name")
        job_title = constant_extract(crawler, config.Carelink_HTML_structure, "job_title")
        job_location = constant_extract(crawler, config.Carelink_HTML_structure, "job_location")
        job_salary = constant_extract(crawler, config.Carelink_HTML_structure, "job_salary")
        job_description = constant_extract(crawler, config.Carelink_HTML_structure, "job_description")
        job_requirement = constant_extract(crawler, config.Carelink_HTML_structure, "job_requirement")
        job_posted_date = constant_extract(crawler, config.Carelink_HTML_structure, "job_posted_date")
        job_expired_date = constant_extract(crawler, config.Carelink_HTML_structure, "job_expired_date")
        contact_name = constant_extract(crawler, config.Carelink_HTML_structure, "contact_name")
        contact_phone = constant_extract(crawler, config.Carelink_HTML_structure, "contact_phone")
        contact_address = constant_extract(crawler, config.Carelink_HTML_structure, "contact_address")
        job = Job(company_name=company_name, job_title=job_title, job_location=job_location, job_salary=job_salary,
                  job_description=job_description, job_requirement=job_requirement,
                  job_posted_date=job_posted_date, job_expired_date=job_expired_date, contact_name=contact_name,
                  contact_phone=contact_phone, contact_address=contact_address, source_link=href,
                  encode_content_hash=sha224(all_content.encode()).hexdigest())
        job.save(True)
    crawler.quit()
    return render(request, "index.html")