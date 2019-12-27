from selenium.webdriver.common.keys import Keys

class InputText:
    def __init__(self, element):
        self.element = element

    def write(self, text):
        """escreve o texto informado"""
        self.element.send_keys(text)

    def submit(self):
        """submete os dados do formulário atual para o servidor"""
        self.element.send_keys(Keys.ENTER)

    def __str__(self):
        return self.element.get_attribute("name")