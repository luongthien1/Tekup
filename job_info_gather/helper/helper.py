from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time

class SeleniumCrawler:
    def __init__(self, visiable=True, size=(1280, 700)) -> None:
        self.options = Options()

        # window size of selenium
        if visiable:
            self.options.add_argument(f"--window-size={size[0]},{size[1]}")
        else:
            self.options.add_argument("--headless")
        # Disable GPU
        # self.options.add_argument("--disable-gpu")
        # Using header to avoid being blocked by web
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) edge/87.0.4280.88 Safari/537.36"
        )
        self.driver = webdriver.Edge(options=self.options)

    def refresh(self):
        self.driver.refresh()

    def crawl(self, url: str, selector: str, script: str = None, sleep: int = 1, check_seletors: list[str] = None):
        # Running URL
        if url != None:
            print("Change url")
            self.driver.get(url)
        # Wait for loading
        time.sleep(sleep)
        if check_seletors != None:
            loop = True
            while loop:
                for check_seletor in check_seletors:
                    if len(self.driver.find_elements(By.CSS_SELECTOR, check_seletor)) != 0:
                        loop = False
                        time.sleep(sleep)
                        break
                if loop:
                    self.refresh()
        if script != None:
            self.driver.execute_script(script)
        # Get elements with css selector corresponding to selector parameter
        els = self.driver.find_elements(By.CSS_SELECTOR, selector)
        return els
#search > div.s-desktop-width-max.s-desktop-content.s-wide-grid-style-t1.s-opposite-dir.s-wide-grid-style.sg-row > div.sg-col-4-of-24.sg-col-4-of-12.s-matching-dir.sg-col-4-of-16.sg-col.sg-col-4-of-20
    # Tương tự crawl ở trên, với nhiệm vụ có thể crawl nhiều selectors
    def crawl_muti_selectors(
        self, url: str, selectors: list[str], script: str = None, sleep: int = 1, check_seletors: list[str] = None
    ):
        # Running URL
        if self.driver.current_url != url:
            self.driver.get(url)
        # Wait for loading
        time.sleep(sleep)
        if check_seletors != None:
            loop = True
            while loop:
                for check_seletor in check_seletors:
                    if len(self.driver.find_elements(By.CSS_SELECTOR, check_seletor)) != 0:
                        loop = False
                        break
                if loop:
                    self.refresh()
        if script != None:
            self.driver.execute_script(script)
        els = []
        for selector in selectors:
            els.append(self.driver.find_elements(By.CSS_SELECTOR, selector))
        return els

    # Tương tự crawl ở trên, với nhiệm vụ có thể crawl nhiều selectors, nhưng toàn bộ elements sẽ nối với nhau thành một danh sách
    def crawl_squence_selectors(
        self, url: str, selectors: list[str], script: str = None, sleep: int = 1,  check_seletors: list[str] = None
    ) -> list[WebElement]:
        # Running URL
        if url != None:
            print("Change url")
            self.driver.get(url)
        # Wait for loading
        time.sleep(sleep)
        if check_seletors != None:
            loop = True
            while loop:
                for check_seletor in check_seletors:
                    if len(self.driver.find_elements(By.CSS_SELECTOR, check_seletor)) != 0:
                        loop = False
                    else:
                        loop = True
                        break
                if loop:
                    self.refresh()
        if script != None:
            self.driver.execute_script(script)
        els = []
        for selector in selectors:
            els += self.driver.find_elements(By.CSS_SELECTOR, selector)
        return els

    # Tắt driver
    def quit(self):
        self.driver.quit()

def check_template(crawl: SeleniumCrawler, url: str, sleep=1, check_exist=list[str], check_no_exist: list[str] = None) -> str:
    crawl.driver.get(url)
    crawl.driver.maximize_window()
    time.sleep(sleep)
    if check_no_exist != None:
        loop = True
        while loop:
            for check_seletor in check_no_exist:
                checking_els = crawl.driver.find_elements(By.CSS_SELECTOR, check_seletor)
                
                if len(checking_els) == 0:
                    loop = False
                    break
            if loop:
                crawl.refresh()
                time.sleep(sleep)
    checking_els = crawl.driver.find_elements(By.CSS_SELECTOR,
                                              "span#inline-twister-expanded-dimension-text-color_name")
    
    if check_exist != None:
            loop = True
            while loop:
                for check_seletor in check_exist:
                    if len(crawl.driver.find_elements(By.CSS_SELECTOR, check_seletor)) != 0:
                        loop = False
                        break
                    else:
                        loop = True
                if loop:
                    crawl.refresh()

    if len(checking_els) == 0:
        return "template1"
    else:
        return "template2"

def check_exist(value, datas):
    for exist_value in datas:
        if value in exist_value:
            return True
    return False

def get_product_code_in_url(url: str) -> str:
    return "/".join(url.split("/")[3:-1])