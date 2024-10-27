from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the driver using WebDriver Manager to automatically manage the ChromeDriver version
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to the Cookie Clicker game page
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Define the IDs for various elements that will be interacted with in the script
cookie_id = "bigCookie"  # ID for the main cookie button to be clicked repeatedly
cookies_id = "cookies"  # ID for the cookie count element
product_price_prefix = "productPrice"  # Prefix for product prices (upgrades)
product_prefix = "product"  # Prefix for the products (upgrades)

# Wait until the language selection element is available and select "English"
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

# Find the language selection button for "English" and click it
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

# Wait until the main cookie element is present on the page
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

# Locate the main cookie element for clicking
cookie = driver.find_element(By.ID, cookie_id)

# Start an infinite loop to keep clicking the cookie and buying upgrades
while True:
    # Click the main cookie to increase the cookie count
    cookie.click()

    # Get the current number of cookies from the cookie count element
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))  # Remove commas and convert to integer

    # Iterate over possible products (upgrades) from 0 to 3 (4 items in total)
    for i in range(4):
        # Get the price of the current product, remove commas, and convert to integer
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        # If the product price is not a digit, skip this iteration (e.g., if the product is unavailable)
        if not product_price.isdigit():
            continue

        # Convert the product price to an integer
        product_price = int(product_price)
        
        # If we have enough cookies to buy the product, click on it
        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break  # Exit the loop once a product is bought

# Pause the script for 10 seconds before quitting (will never reach here due to infinite loop)
time.sleep(10)

# Close the browser (this line will not be reached because of the infinite loop)
driver.quit()
