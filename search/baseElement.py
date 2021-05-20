from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BaseElement(object):
    def __init__(self, driver, by, value):
        self.driver = driver
        self.by = by
        self.value = value
        self.locator = (self.by, self.value)

    
    def click(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        element.click
        return None

    def text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locator)
        )
        return element.text