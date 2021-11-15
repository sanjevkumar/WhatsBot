import random
from time import time,ctime,sleep

from selenium import webdriver
from selenium_stealth import stealth

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException


drivpath = '\WhatsBot\chromedriver.exe')
username = ''


def connect():
    driver.get("https://web.whatsapp.com/")
    while True:
        try:
            status = driver.find_element(By.CLASS_NAME, '_2dfCc').text
            print(status+"...", end='\r', flush=True)
        except StaleElementReferenceException:
            try:
                driver.implicitly_wait(15)
                driver.find_element(By.CLASS_NAME, '_2dfCc').text
            except StaleElementReferenceException:
                break
            except NoSuchElementException:
                break
        except NoSuchElementException:
            try:
                driver.implicitly_wait(15)
                status = driver.find_element(By.CLASS_NAME, '_2dfCc').text
                print(status, end='\r', flush=True)
            except NoSuchElementException:
                break
    try:
        driver.implicitly_wait(60)
        whatstext = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[4]/div/div/div[2]/div[1]/h1').text
        if whatstext == "WhatsApp Web":
            print("\nLogin SuccessFull")
    except NoSuchElementException:
        print("Waiting")
        driver.implicitly_wait(60)
        whatstext = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[4]/div/div/div[2]/div[1]/h1').text
        if whatstext == "WhatsApp Web":
            print("\nLogin SuccessFull")


def message():
    messages = ["Sorry Sanjev is sleeping now -SmartBot", "Sanjev is unavailable please text later -SmartBot", "Sanjev is busy right now Please text later -SmartBot"]
    while True:
        sleep(3)
        print("\n\nChecking For New Message\n")
        try:
            msgcount = driver.find_element(By.CLASS_NAME, "_23LrM").text
            driver.find_element(By.CLASS_NAME, "_23LrM").click()
        except NoSuchElementException:
            print("No New Messages")
        if int(msgcount) >= 1:
            break
    try:
        name = driver.find_element(By.CLASS_NAME, "_21nHd").text
        print(name+", Msgs: "+msgcount)
    except NoSuchElementException:
        print("Error Please Restart (or) Check Element")
    msg = random.choice(messages)
    print("Reply: "+msg.format(username))
    try:
        entertxt = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
        entertxt.send_keys(msg.format(username))
        driver.find_element(By.CLASS_NAME, "_4sWnG").click()
    except NoSuchElementException:
        print("Unable To Sent Message")
    message()


# In The Beginning //
print('\n')
print("     *       * *    *     *     ******* *******     *     ******* *******    ******  ******* *******     ")
print("     *   *   * *    *    * *       *    *          * *    *     * *     *    *     * *     *    *        ")
print("     *  * *  * ******   *****      *    *******   *****   ******* *******    ******  *     *    *        ")
print("     * *   * * *    *  *     *     *          *  *     *  *       *          *     * *     *    *        ")
print("     **     ** *    * *       *    *    ******* *       * *       *          ******  *******    *        ")
print(" "*39+"Google Meet Automater by SmartSanjev"+" "*39, end='\n\n')
t = time()
print(" "*33+"Current Time: ",ctime(t))
print("-" * 105, end='\n\n')

# creating Chrome instance
opt = Options()
# opt.add_argument('--disable-blink-features=AutomationControlled')
# opt.add_experimental_option("debuggerAddress","localhost:9222")
# opt.add_argument('--headless')
opt.add_experimental_option('useAutomationExtension', False)
opt.add_argument("start_maximized")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("user-data-dir=C:\\Users\\smart\\AppData\\Local\\Google\\Chrome\\User Data")
# opt.add_experimental_option('useAutomationExtension', False)
ser = Service(drivpath)
driver = webdriver.Chrome(options=opt,service=ser)



connect()
message()
