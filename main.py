import time
import random
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
pin = '2160667'
names = []
with open("names.txt", "r") as f:
    for line in f:
        names.append(line.replace("\n", ""))
random.shuffle(names)


class main:
    def __init__(self, username, num):
        self.username = username
        self.num = num
        threading.Thread(target=self.start).start()
        #self.start()

    def start(self):
        while True:
            try:
                self.browser = webdriver.Chrome(options=options)
                break
            except:
                pass
        self.browser.get("https://kahoot.it")
        self.browser.find_element_by_xpath('//*[@id="game-input"]').send_keys(pin)
        self.browser.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[3]/div[2]/main/div/form/button').click()
        while True:
            try:
                self.browser.find_element_by_xpath('//*[@id="nickname"]').send_keys(f'{self.username} {self.num}')
                break
            except:
                pass
        self.browser.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[3]/div[2]/main/div/form/button').click()
        print(f"{self.num} is in")
        while True:
            while True:
                try:
                    if self.browser.find_element_by_xpath(
                            '//*[@id="root"]/div[1]/main/div[2]/div/div') is not None and (len(
                        self.browser.find_elements_by_xpath(
                            '//*[@id="root"]/div[1]/main/div[2]/div/div/*')) == 4 or len(
                        self.browser.find_elements_by_xpath(
                            '//*[@id="root"]/div[1]/main/div[2]/div/div/*')) == 2):
                        break
                except:
                    pass
            elms = self.browser.find_elements_by_xpath('//*[@id="root"]/div[1]/main/div[2]/div/div/*')
            choice = random.randint(0, len(elms) - 1)
            elms[choice].click()
            while True:
                try:
                    if self.browser.find_element_by_xpath('//*[@id="root"]/div[1]/main/div[2]/h1/div/p[1]') is not None:
                        break
                except:
                    pass


#main("test", '1')
m = []
for k in range(0, 10):
    for i, v in enumerate(names):
        m.append(main(v, str(k+1)))

