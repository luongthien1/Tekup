from helper.helper import SeleniumCrawler
from selenium.webdriver.common.by import By
import os
from huggingface_hub import login
from config.config import constant_website, questions
from transformers import pipeline

def geturl(url: str, page: int):
    return url.format(page=page)

def extract_info(crawler: SeleniumCrawler, selector:str, HTML_structure: dict, key: str, website: str = "careerlink"):
    if website in constant_website:
        return constant_extract(crawler, HTML_structure, key, website)
    else:
        return dynamic_extract(crawler, selector, key)
def constant_extract(crawler: SeleniumCrawler, HTML_structure: dict, key: str, website: str = "careerlink"):
    list_el = crawler.crawl_squence_selectors(None, HTML_structure[key]["selector"])
    if not HTML_structure[key]["label"]:
        return aextract(website, key, "\n".join([el.text for el in list_el]))
    elif len(HTML_structure[key]["selector"]) == 1:
        results = []
        list_parent_el = crawler.crawl_squence_selectors(None, HTML_structure[key]["container"]["selector"])
        for i in range(len(list_parent_el)):
            if "existed" in HTML_structure[key]["label"]:
                if list_parent_el[i].find_elements(By.CSS_SELECTOR, HTML_structure[key]["label"]["existed"]["selector"]):
                    els = list_parent_el[i].find_elements(By.CSS_SELECTOR, HTML_structure[key]["container"]["to_info"])
                    text = "".join([el.text for el in els])
                    info = aextract(website, key, text)
                    results.append(info)
        return "\n".join(results)

def dynamic_extract(crawler: SeleniumCrawler, selector: str, key: str):

    login(token="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")
    # model_checkpoint = "nguyenvulebinh/vi-mrc-large"
    model_checkpoint = "nguyenvulebinh/vi-mrc-base"
    nlp = pipeline('question-answering', model=model_checkpoint,
                    tokenizer=model_checkpoint)
    question = questions[key]
    context = crawler.crawl(None, selector)[0].text
    QA_input = {
        'question': question,
        'context': context
    }
    res = nlp(QA_input)
    threshold = 0.003968983422964811
    if res["score"] > threshold:
        return res["answer"]
    # threshold: 0.003968983422964811 -> Không tìm thấy thông tin liên quan

def aextract(website: str, key: str, text: str):
    if website == "careerlink":
        return carelink_aextract(key, text)
    else:
        return text

def carelink_aextract(key, text):
    if key == "job_title":
        info = text.split("\n")[0]
    if key == "job_posted_date":
        info = text.split("\n")[-1]
    else:
        info = text
    return info
