from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace with your own ChromeDriver path
PATH = "C:/Users/frost/automation-journey/scripts/drivers/chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(3)

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, f"productPrice{i}") for i in range (1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)


# link = driver.find_element(By.LINK_TEXT, "Dog")
# link.click()

# try:
#     element = WebDriverWait(driver, 2).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Contact"))
#     )
#     element.click()

#     element = WebDriverWait(driver, 2).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Home"))
#     )
#     element.click()

#     element = WebDriverWait(driver, 2).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Dog"))
#     )
#     element.click()

#     element = WebDriverWait(driver, 2).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Dog Breeds"))
#     )
#     element.click()

#     element = WebDriverWait(driver, 2).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "German Shepherd"))
#     )
#     element.click()

#     element = WebDriverWait(driver, 2).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Labrador Retriever"))
#     )
#     element.click()

#     element = WebDriverWait(driver, 2).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Akita Inu"))
#     )
#     element.click()

# except:
#     driver.quit()

# print(driver.title)

# try:
#     main = WebDriverWait(driver, 3).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "md-main"))
#     )

#     articles = main.find_elements(By.TAG_NAME, "article")
#     for article in articles:
#         header = article.find_element(By.CSS_SELECTOR, ".md-content__inner.md-typeset")
#         print(header.text)
# finally:
#     driver.quit()

# try:
#     search = WebDriverWait(driver, 2).until(
#         EC.presence_of_element_located((By.NAME, "query"))
#     )
#     search.click()
#     time.sleep(2)
#     search = driver.find_element(By.NAME, "query")
#     search.send_keys("German Shepherd")
#     search.send_keys(Keys.RETURN)
#     time.sleep(2)
# finally:
#     driver.quit()

# search = driver.find_element(By.NAME, "query")
# search.send_keys("Selenium Playground")
# search.send_keys(Keys.RETURN)

driver.quit()