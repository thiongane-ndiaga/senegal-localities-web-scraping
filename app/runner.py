from datetime import datetime
import json
from chrome_driver_manager import AppChromeDriverManager
from constants import locators
from selenium.webdriver.common.by import By
from helpers.logging import logger
from helpers.os import project_root_path
if __name__ == "__main__":
    locations_list = []

    chrome = AppChromeDriverManager()

    for page in range(5):
        url = f"https://hcct.sn/territoires/collectivit%C3%A9s-territoriales?page={page}"
        print(f"Will navigate to {url}")
        chrome.navigate_to(url)

        container_we = chrome.wait_visibility_of_element(
            30, locators.DIV_CONTAINER)
        if container_we:

            department_span_list = chrome.get_elements(
                locators.SPAN_DEPARTMENT_ROW)
            for i in range(len(department_span_list)):
                i1 = i+1
                xpath = f"({locators.SPAN_DEPARTMENT_ROW[1]})[{i1}]{locators.A_DEPARTMENT[1]}"
                department_a = chrome.get_element((By.XPATH, xpath))

                xpath = f"({locators.SPAN_DEPARTMENT_ROW[1]})[{i1}]{locators.DIV_COMMUNE[1]}"

                commune_div_list = chrome.get_elements((By.XPATH, xpath))
                print(
                    f"\n{i1} - {department_a.text} : {len(commune_div_list)} communes")
                for j in range(len(commune_div_list)):
                    commune_div = commune_div_list[j]
                    print("==> ", commune_div.text)
                    locations_list.append(
                        {"id": i*100+j+1, "department": department_a.text, "name": commune_div.text})

    logger.info(f"Scraping done : found {len(locations_list)} 'communes'")
    if locations_list:
        ts = int(datetime.now().timestamp())
        filename = f'{project_root_path}/data/communes-{ts}.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(locations_list, f, ensure_ascii=False, indent=4)
            logger.info(f"Created {filename}")
