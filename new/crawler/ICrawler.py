from selenium import webdriver
from pyvirtualdisplay import Display


class ICrawler:
    def __init__(self):
        display = Display(visible=0, size=(800, 600))
        display.start()
        self.brower = webdriver.Firefox()

    def craw_base(self):
        pass

    def craw_every_day(self):
        pass
