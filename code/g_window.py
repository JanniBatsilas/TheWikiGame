from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from _thread import *


class GameWindow:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.driver.get("https://de.wikipedia.org/wiki/Einhorn")
        start_new_thread(self.window_listener, ())


    def window_listener(self):
        while True:
            print(self.driver.current_url)
            time.sleep(1)








