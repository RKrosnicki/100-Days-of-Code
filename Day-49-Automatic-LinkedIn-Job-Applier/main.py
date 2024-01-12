from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time


def click_save():
    button = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
    button.click()


def click_follow():
    company_button = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/div/a')
    company_button.click()
    time.sleep(5)
    follow = driver.find_element(By.CLASS_NAME, 'follow')
    follow.click()


login = os.environ['DUMMY_EMAIL']
password = os.environ['DUMMY_LINKEDIN_PWD']
search_URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3798816050&distance=25&f_AL=true&geoId=105072130&keywords=python%20developer&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true'


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.linkedin.com/')

email_input = driver.find_element(By.ID, 'session_key')
email_input.send_keys(login)
time.sleep(5)
password_input = driver.find_element(By.ID, 'session_password')
password_input.send_keys(password)
time.sleep(5)
password_input.send_keys(Keys.ENTER)
time.sleep(5)
time.sleep(20)
driver.get(search_URL)
time.sleep(5)

full_list = driver.find_elements(By.CLASS_NAME, 'job-card-container')

# Uncomment this to save all, and follow employers

# for i in range(len(full_list)):
#     full_list = driver.find_elements(By.CLASS_NAME, 'job-card-container')
#     full_list[i].click()
#     time.sleep(5)
#     click_save()
#     click_follow()
#     driver.get(search_URL)
#     time.sleep(5)

# Uncomment this to fill a form, where 1st step is to input number, then review resumee, and final step is acceptance.

# full_list[1].click()
# time.sleep(2)
# apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
# apply_button.click()
# time.sleep(2)
# phone_input = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[4]/div/div/div[1]/div/input')
# phone_input.send_keys('123456789')
# driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button').click()
# time.sleep(2)
# second_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
# second_button.click()
# time.sleep(2)
# final_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[2]/button[2]')
# #  #final_button.click()
# print("I'm not going to spam here, but I could")
# ex_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/button')
# ex_button.click()
