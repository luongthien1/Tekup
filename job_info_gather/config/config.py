constant_website = ["careerlink"]

questions = {
    "job_title": "Vị trí công việc là gì?",
    "company_name": "Tên công ty là gì?",
    "job_location": "Địa chỉ làm việc ở đâu?",
    "job_salary": "Mức lương bao nhiêu?",
    "experience": "Yêu cầu kinh nghiệm là gì?",
    "job_posted_date": "Ngày đăng tuyển dụng?",
    "job_expired_date": "Hạn nộp hồ sơ?",
    "job_description": "Mô tả công việc?",
    "job_requirement": "Yêu cầu công việc?",
    "contact_name": "Tên người liên hệ?",
    "contact_phone": "Số điện thoại liên hệ?",
    "contact_address": "Địa chỉ liên hệ?",
}

Facebook_url = "https://www.facebook.com/careerlink.vn"
Facebook_selector_info_url = "#mount_0_0_NE > div > div:nth-child(1) > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x78zum5.xdt5ytf.x1iyjqo2.x1us19tq > div > div.x9f619.x2lah0s.x1n2onr6.x78zum5.x1iyjqo2.x1t2pt76.x1lspesw > div > div > div.x78zum5.xdt5ytf.x1iyjqo2 > div > div > div.x6s0dn4.x78zum5.xdt5ytf.xwib8y2.xh8yej3 > div > div > div.x9f619.x1n2onr6.x1ja2u2z.xeuugli.xs83m0k.x1xmf6yo.x1emribx.x1e56ztr.x1i64zmx.xjl7jj.x19h7ccj.xu9j1y6.x7ep2pv > div:nth-child(2) > div:nth-child(2) > div > div > div > div > div > div > div > div > div > div > div:nth-child(2) > div > div > div:nth-child(2) > div > div.x1iyjqo2 > div > div:nth-child(2) > span > span > span:nth-child(2) > span > a"

Carelink_url = "https://www.careerlink.vn/tim-viec-lam-tai/da-nang/DN?page={page}"
selector_info_url = "body > div.container.mt-3.mt-lg-4 > div > div.col-lg-9.px-0.px-lg-3 > ul > li > div > div.media-body.overflow-hidden > a.job-link.clickable-outside"

Carelink_HTML_structure = {
    "all_content": {
        "selector": ["#jd-col > div > div.card.border-0.font-nunitosans.px-4 > div.job-detail-body.py-2"],
        "label": None
    },
    "job_title": {
        "selector": ["#jd-col > div > div.card.border-0.font-nunitosans.px-4 > div.job-detail-header.mt-3 > div.media.row.m-0 > div.media-body.job-title-and-org-name > div > h1"],
        "label": None
    },
    "company_name": {
        "selector": ["#jd-col > div > div.card.border-0.font-nunitosans.px-4 > div.job-detail-header.mt-3 > div.media.row.m-0 > div.media-body.job-title-and-org-name > p > a > span"],
        "label": None
    },
    "job_location": {
        "selector": ["#jd-col > div > div.card.border-0.font-nunitosans.px-4 > div.job-detail-header.mt-3 > div.job-overview.mt-2 > div.d-flex.align-items-start.mb-2 > span"],
        "label": {
            "existed": {
                "selector": "i.cli-map-pin-line",
            },
        },
        "container": {
            "selector": ["#jd-col > div > div.card.border-0.font-nunitosans.px-4 > div.job-detail-header.mt-3 > div.job-overview.mt-2 > div.d-flex.align-items-start.mb-2"],
            "to_info": "span"
        }
    },
    "job_salary": {
        "selector": ["#jd-col > div > div.card.border-0.font-nunitosans.px-4 > div.job-detail-header.mt-3 > div.job-overview.mt-2 > div > span.text-primary"],
        "label": {
            "existed": {
                "selector": "i.cli-currency-circle-dollar",
            },
        },
        "container": {
            "selector": ["#jd-col > div > div.card.border-0.font-nunitosans.px-4 > div.job-detail-header.mt-3 > div.job-overview.mt-2 > div"],
            "to_info": "span.text-primary"
        }
    },
    "experience": {
        "selector": ["#jd-col > div > div.card.border-0.font-nunitosans.px-4 > div.job-detail-header.mt-3 > div.job-overview.mt-2 > div:nth-child(3) > span"],
        "label": {
            "existed": {
                "selector": "i.cli-suitcase-simple",
            },
        },
        "container": {
            "selector": ["#jd-col > div > div.card.border-0.font-nunitosans.px-4 > div.job-detail-header.mt-3 > div.job-overview.mt-2 > div.d-flex.align-items-start.mb-2"],
            "to_info": "span.text-primary"
        }
    },
    "job_posted_date": {
        "selector": ["#jd-col > div > div.card.border-0.font-nunitosans.px-4 > div.job-detail-header.mt-3 > div.job-overview.mt-2 > div > div.date-from.d-flex.align-items-center > span"],
        "label": None
    },
    "job_expired_date": {
        "selector": ["#jd-col > div > div.card.border-0.font-nunitosans.px-4 > div.job-detail-header.mt-3 > div.job-overview.mt-2 > div > div.day-expired.d-flex.align-items-center > span > b"],
        "label": None
    },
    "job_description": {
        "selector": ["#section-job-description > div.my-3", "#section-job-benefits > div.my-3"],
        "label": None
    },
    "job_requirement": {
        "selector": ["#section-job-skills > div.raw-content.rich-text-content > p"],
        "label": None
    },
    "contact_name": {
        "selector": ["#section-job-contact-information > ul > li > span"],
        "label": {
            "existed": {
                "selector": "div > i.cli-contact-with",
            },
        },
        "container": {
            "selector": ["#section-job-contact-information > ul > li.align-items-start"],
            "to_info": "span.person-name"
        }
    },
    "contact_phone": {
        "selector": ["#section-job-contact-information > ul > li > span"],
        "label": {
            "existed": {
                "selector": "div > i.cli-phone",
            },
        },
        "container": {
            "selector": ["#section-job-contact-information > ul > li.align-items-start"],
            "to_info": "span"
        }
    },
    "contact_address": {
        "selector": ["#section-job-contact-information > ul > li > span"],
        "label": {
            "existed": {
                "selector": "div > i.cli-location",
            },
        },
        "container": {
            "selector": ["#section-job-contact-information > ul > li.align-items-start"],
            "to_info": "span"
        }
    },
}