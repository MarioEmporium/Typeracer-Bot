from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time
from bs4 import BeautifulSoup
from lxml import etree
#Change to whatever path you have chromium
driver = webdriver.Chrome(executable_path='C:\\Users\\Jack\\Documents\\Chromium\\chromedriver_win32\\chromedriver.exe')
driver.get("https://play.typeracer.com/")
keyboard = Controller()
time.sleep(3)

#Start a race
keyboard.press(Key.ctrl)
keyboard.press(Key.alt_l)
keyboard.press('i')

keyboard.release(Key.ctrl)
keyboard.release(Key.alt_l)
keyboard.release('i')
time.sleep(2)


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
dom = etree.HTML(str(soup))


#Grab the paragraph to type
wordLength = len(dom.xpath('//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div')[0])
firstLetter = dom.xpath('//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]')[0].text

if(wordLength > 2):
    restOfFirstWord = dom.xpath('//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]')[0].text
    text = dom.xpath('//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]')[0].text
else:
    restOfFirstWord = ''
    text = dom.xpath('//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]')[0].text

fullText = firstLetter + restOfFirstWord + text

#Wait for the race to start
raceStarted = dom.xpath('//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')[0].attrib['class']

while raceStarted == "txtInput txtInput-unfocused":
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    dom = etree.HTML(str(soup))
    raceStarted = dom.xpath('//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')[0].attrib['class']

#Type the characters lightning fast
for char in fullText:
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(.016)

#Admire your achievment
time.sleep(5)
driver.close()