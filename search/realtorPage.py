from selenium.webdriver.common.by import By
from lxml import etree
from .baseElement import BaseElement

class RealtorPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def go(self):
        self.driver.get(self.url)

    def list_elements(self, locator):
        page=etree.HTML(self.driver.page_source)
        return page.findall(locator)

    def rentals(self, locator):
        plans = []
        for bedroom in self.list_elements(locator):
            result = ''
            for info in bedroom.findall("./td"):
                if info.text.strip() != '':
                    result += info.text.strip() + ' | '
            plans.append(result)
        return plans
    
    def comm_features(self, locator):
        community = []
        for list_prop in self.list_elements(locator)[0:2]:
            for x in list_prop.findall("./li"):
                community.append (x.text)

        return community

    def unit_features(self, locator):
        unit = []
        for list_prop in self.list_elements(locator)[2:4]:
            for x in list_prop.findall("./li"):
                unit.append (x.text)
        return unit

    def apartment(self):
        locator = (By.XPATH, ".//div[@data-original-title='Apartment']")
        return BaseElement (
            driver=self.driver,
            by=locator[0],
            value=locator[1]
        )


    def address(self, addr):
        locator = (By.XPATH, ".//span[@itemprop='{}']".format(addr))
        return BaseElement (
            driver=self.driver,
            by=locator[0],
            value=locator[1]
        )

    def name(self):
        locator = (By.XPATH, ".//h1[@itemprop='address']/span")
        return BaseElement (
            driver=self.driver,
            by=locator[0],
            value=locator[1]
        )

    def description(self):
        locator = (By.ID, "ldp-detail-romance")
        return BaseElement(
            driver=self.driver,
            by=locator[0],
            value = locator[1]
        )

    def format_address(self):
        return (self.address("streetAddress").text() + " " + 
        self.address("addressLocality").text() + ", " + 
        self.address("addressRegion").text() + " " + 
        self.address("postalCode").text())

    def format_plan(self, plan = 'studio'):
        if plan == 'studio':
            return ".//div[@id = 'content-floorplan-studio']/div/table/tbody/tr"
        else:
            return ".//div[@id = 'content-floorplan-{}-bedroom']/div/table/tbody/tr".format(plan)