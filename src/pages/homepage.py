from pages.page import Page
from elements.inputtext import InputText
from main import DRIVE_PATH
from selenium import webdriver

class HomePage(Page):

    def __init__(self):
        self.driver = webdriver.Chrome(DRIVE_PATH)
    
    def search(self, criteria):
        super().navigate("https://www.google.com.br")

        assert self.driver.title == "Google"

        a = InputText(self.driver.find_element_by_xpath("//input[@name='q']"))
        a.write(criteria)
        a.submit()

        el = self.driver.find_elements_by_xpath("//div[@class='r']")
        ret = []

        for i in el:
            name = i.find_element_by_tag_name("h3").text
            link = i.find_element_by_tag_name("a").get_attribute("href")

            ret.append(f"{name}\t{link}")

        return ret