from selenium import webdriver
from main import DRIVE_PATH

class Page:
    def __init__(self):
        self.driver = webdriver.Chrome(DRIVE_PATH)

    def __str__(self):
        return "Teste"

    def __del__(self):
        del self.driver

    def navigate(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()