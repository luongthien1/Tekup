from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from models.models import Job, Website
from helper.helper import SeleniumCrawler
from helper.extract import extract_info, geturl
from hashlib import sha224
from django.core import serializers
import json
import config.config as config
import typing
# Create your views here.
class AdminApp:
    def index(request):
        respone = AdminApp.additional_respone({})
        return render(request, "admins/index.html", respone)

    def api_crawl(request: HttpRequest):
        if request.method == "POST":
            if "action" in request.POST:
                action = request.POST["action"]
                if action == "crawl":
                    respone = AdminApp.crawl(request)
        AdminApp.additional_respone(respone)
        return JsonResponse(respone)
        
    def crawl(request: HttpRequest):
        try:
            crawler = SeleniumCrawler()
            respone = {"results": []}
            data : typing.Mapping = AdminApp.preprocess_request(request)
            max_post_number = data.get("max_post_number", 0)
            selector = data.get("selector")
            info_url_selector = data.get("info_url_selector")
            url = data.get("website_url")
            show_more_mode = data.get("show_more_mode")
            website = url.split("/")[2].split(".")[1]

            while len(respone["results"]) < int(max_post_number):
                info_blocks = crawler.crawl(geturl(url, 1), info_url_selector)
                hrefs = [info_block.get_attribute("href") for info_block in info_blocks]
                for href in hrefs:
                    if len(respone["results"]) >= int(max_post_number):
                        break
                    crawler.driver.get(href)
                    all_content = extract_info(crawler, selector, config.Carelink_HTML_structure, "all_content", website)
                    if Job.objects.filter(encode_content_hash=sha224(all_content.encode()).hexdigest()).exists():
                        continue
                    company_name = extract_info(crawler, selector, config.Carelink_HTML_structure, "company_name", website)
                    job_title = extract_info(crawler, selector, config.Carelink_HTML_structure, "job_title", website)
                    job_location = extract_info(crawler, selector, config.Carelink_HTML_structure, "job_location", website)
                    job_salary = extract_info(crawler, selector, config.Carelink_HTML_structure, "job_salary", website)
                    job_description = extract_info(crawler, selector, config.Carelink_HTML_structure, "job_description", website)
                    job_requirement = extract_info(crawler, selector, config.Carelink_HTML_structure, "job_requirement", website)
                    job_posted_date = extract_info(crawler, selector, config.Carelink_HTML_structure, "job_posted_date", website)
                    job_expired_date = extract_info(crawler, selector, config.Carelink_HTML_structure, "job_expired_date", website)
                    contact_name = extract_info(crawler, selector, config.Carelink_HTML_structure, "contact_name", website)
                    contact_phone = extract_info(crawler, selector, config.Carelink_HTML_structure, "contact_phone", website)
                    contact_address = extract_info(crawler, selector, config.Carelink_HTML_structure, "contact_address", website)
                    job = Job(company_name=company_name, job_title=job_title, job_location=job_location, job_salary=job_salary,
                            job_description=job_description, job_requirement=job_requirement,
                            job_posted_date=job_posted_date, job_expired_date=job_expired_date, contact_name=contact_name,
                            contact_phone=contact_phone, contact_address=contact_address, source_link=href,
                            encode_content_hash=sha224(all_content.encode()).hexdigest())
                    
                    respone["results"].append(json.loads(serializers.serialize("json", [job]))[0]["fields"])
        except Exception as e:
            respone["error"] = f"An error occurred: {e}"
        finally:
            crawler.quit()
        return respone
    
    def preprocess_request(request: HttpRequest):
        data = request.POST.copy()
        show_more_mode = data.get("show_more_mode")
        if show_more_mode == Website.Constants.SHOW_MORE_PAGE:
            if "{page}" not in data["website_url"]:
                if "?" in data["website_url"]:
                    data["website_url"] += "&"
                else:
                    data["website_url"] += "?"
                data["website_url"] += "page={page}"
        return data

    def additional_respone(respone):
        respone["show_more_options"] = [value for name, value in vars(Website.Constants).items() if not name.startswith('_')]
        return respone