from selenium.webdriver.common.by import By

DIV_CONTAINER = (By.CLASS_NAME, "container")
SPAN_DEPARTMENT_ROW = (
    By.XPATH, '//h5[@class="header"]//a/ancestor::span[@class="field-content"]')
A_DEPARTMENT = (By.XPATH, '//h5[@class="header"]//a')
DIV_COMMUNE = (By.XPATH, '//div[@class="commune"]')
