from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, 'cookie')

now = datetime.now()
t_end = now + timedelta(minutes=5)

while datetime.now() < t_end:
    cookie.click()
    if datetime.now().second % 5 == 0:
        upgrades = driver.find_elements(By.XPATH, "/html/body/div[3]/div[5]/div/div[not(@class='grayed')]")
        if len(upgrades) > 0:
            upgrades[-1].click()
        time.sleep(0.01)

