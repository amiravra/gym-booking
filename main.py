import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Add your credentials at the top of your script
ACCOUNT_EMAIL = "your_email@test.com"  # The email you registered with
ACCOUNT_PASSWORD = "PassTest1!"      # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"


#keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#have chrome store my profile
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

#open chrome and go to the gym website
driver = webdriver.Chrome(options=chrome_options)
driver.get(url= GYM_URL)

#login to the gym
register_button = driver.find_element(By.XPATH, value="//*[@id='home-page']/section[1]/div/div/a[1]/button")
register_button.click()
email = driver.find_element(By.ID, value="email-input")
password = driver.find_element(By.NAME, value="password")
login = driver.find_element(By.ID, value="submit-button")
email.send_keys(ACCOUNT_EMAIL)
password.send_keys(ACCOUNT_PASSWORD)
login.click()