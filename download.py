from selenium import webdriver
import time
import os


class DownloadBot:
    def __init__(self):
        self.links = []
        self.downpath = os.getcwd() + '\\torrent\\'
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": self.downpath}
        chromeOptions.add_experimental_option("prefs", prefs)
        f = open("game-files.txt", 'r')
        for i in f:
            self.links.append(i.rstrip('\n'))
        f.close()
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)

    def startDown(self):
        self.driver.get(f"https://freetp.org/")
        for i in self.links:
            self.driver.get(f"https://freetp.org/{i}")
            time.sleep(15)
            self.driver.find_element_by_xpath('//input[@type="submit"]').click()
            time.sleep(1)

    def addToTorrent(self):
        files = os.listdir(self.downpath)
        for i in files:
            os.startfile(self.downpath + i)

# db = DownloadBot()
# db.startDown()
# db.addToTorrent()
