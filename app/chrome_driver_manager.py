from typing import List
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException


from helpers.logging import logger
from helpers.os import project_root_path


class AppChromeDriverManager():
    def __init__(self):
        self.driver: Chrome = self.get_driver()

    def get_driver(self):
        """Create an instance of the Chrome driver

        Returns:
            Chrome: the instance of the Chrome WebDriver
        """
        options = Options()
        """options.add_argument(
            "user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")"""
        options.add_argument('--start-maximized')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")

        options.binary_location = f"{project_root_path}/browsers/chrome-mac-x64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
        driver_path = f"{project_root_path}/browsers/chromedriver-mac-x64/chromedriver"

        service = Service(driver_path)
        driver = Chrome(service=service, options=options)
        return driver

    def navigate_to(self, url: str):
        """Loads a web page in the current browser session.

        Args:
            url (str): the URL of the web page
        """
        self.driver.get(url)

    def wait_presence_of_element(self, timeout: int, locator: tuple) -> WebElement:
        """Wait for the element to be located in the page

        Args:
            driver (WebDriver): the instance of WebDriver
            timeout (int): the number of seconds before timing out
            locator (tuple): used to find the element, e.g (By.XPATH, xpath)

        Returns:
            WebElement|None : the WebElement if located or None otherwise
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator))
            return element
        except Exception:
            logger.error("in wait_presence_of_element :")
            return None

    def wait_presence_of_all_elements(self, timeout: int, locator: tuple) -> List[WebElement]:
        """Wait for all specific elements to be located in the page

        Args:
            driver (WebDriver): the instance of WebDriver 
            timeout (int): the number of seconds before timing out
            locator (tuple): used to find the element, e.g (By.XPATH, xpath)

        Returns:
            WebElement[]|None : the WebElements List if located or None otherwise
        """
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator))
            return elements
        except Exception:
            return None

    def wait_visibility_of_element(self, timeout: int, locator: tuple, web_element: WebElement = None) -> WebElement:
        """Wait for the element to be visible on the page

        Args:
            driver (WebDriver): the instance of WebDriver 
            timeout (int): the number of seconds before timing out
            locator (tuple): used to find the element, e.g (By.XPATH, xpath)

        Returns:
            WebElement|None : the WebElement if located or None otherwise
        """
        try:
            element = WebDriverWait(web_element or self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            return element
        except Exception:
            return None

    def wait_visibility_of_all_elements(self, timeout: int, locator: tuple) -> List[WebElement]:
        """Wait for all specific elements to be visible on the page

        Args:
            driver (WebDriver): the instance of WebDriver 
            timeout (int): the number of seconds before timing out
            locator (tuple): used to find the element, e.g (By.XPATH, xpath)

        Returns:
            WebElement[]|None : the WebElements List if located or None otherwise
        """
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator))
            return elements
        except Exception:
            return None

    def get_element(self, locator: tuple, web_element: WebElement = None) -> WebElement:
        """Finds and returns the WebElement

        Args:
            driver (WebDriver): the instance of WebDriver 
            locator (tuple): used to find the element, e.g (By.XPATH, xpath)

        Returns:
            WebElement|None : the WebElement if found or None otherwise
        """
        try:
            driver = web_element or self.driver
            element = driver.find_element(locator[0], locator[1])
            return element
        except Exception:
            return None

    def get_elements(self, locator: tuple, web_element: WebElement = None) -> List[WebElement]:
        """Finds and returns the WebElement List

        Args:
            driver (WebDriver): the instance of WebDriver 
            locator (tuple): used to find the elements, e.g (By.XPATH, xpath)

        Returns:
            WebElement|None : the WebElement List if found or None otherwise
        """
        try:
            driver = web_element or self.driver
            element = driver.find_elements(locator[0], locator[1])
            return element
        except:
            return None
