from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import requests 

driver = webdriver.Chrome()
driver.get('https://selectorshub.com/xpath-practice-page/')

# Find the shadow host element
shadow_host = driver.find_element(By.CSS_SELECTOR, "#userName").shadow


# Optional: Pause for a few seconds to observe the action (for debugging purposes)
time.sleep(2)

# Close the browser after action is completed
driver.quit()