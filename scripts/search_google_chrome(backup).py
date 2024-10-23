from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Set up the Chrome WebDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Step 2: Open Google
    driver.get("https://www.google.com")

    # Step 3: Find the search bar using its name attribute value and search for "Selenium Python"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)

    # Step 4: Explicit wait for the first search result to be present
    wait = WebDriverWait(driver, 10)
    first_result = wait.until(EC.presence_of_element_located((By.XPATH, "//h3")))

    # Step 5: Click on the first search result link
    first_result.click()

    # Step 6: Wait for the new page to load and print the title
    wait.until(EC.title_contains("Selenium"))
    print("New Page Title:", driver.title)

finally:
    # Step 7: Close the browser
    driver.quit()
