from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time

# Set up the driver using WebDriver Manager to automatically manage the ChromeDriver version
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to the Cookie Clicker game page
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Define the IDs for various elements that will be interacted with in the script
cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

# Wait until the language selection element is available and select "English"
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
    )
    # Find the language selection button for "English" and click it
    language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
    language.click()
except TimeoutException:
    print("Language selection took too long.")
    driver.quit()
    exit()

# Wait until the main cookie element is present on the page
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, cookie_id))
    )
except TimeoutException:
    print("Cookie element took too long to load.")
    driver.quit()
    exit()

# Start an infinite loop to keep clicking the cookie and buying upgrades
try:
    while True:
        # Try to locate the main cookie element and click it
        try:
            cookie = driver.find_element(By.ID, cookie_id)
            cookie.click()
        except StaleElementReferenceException:
            # If the element goes stale, continue and re-fetch in the next loop iteration
            continue

        # Get the current number of cookies from the cookie count element
        try:
            cookies_count_text = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
            cookies_count = int(cookies_count_text.replace(",", ""))
        except StaleElementReferenceException:
            # If the cookies count element goes stale, skip this iteration
            continue

        # Iterate over possible products (upgrades) from 0 to 3 (4 items in total)
        for i in range(4):
            try:
                # Get the price of the current product, remove commas, and convert to integer
                product_price_text = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

                # If the product price is not a digit, skip this iteration (e.g., if the product is unavailable)
                if not product_price_text.isdigit():
                    continue

                # Convert the product price to an integer
                product_price = int(product_price_text)

                # If we have enough cookies to buy the product, click on it
                if cookies_count >= product_price:
                    product = driver.find_element(By.ID, product_prefix + str(i))
                    product.click()
                    break  # Exit the loop once a product is bought
            except StaleElementReferenceException:
                # Handle stale element by continuing to the next iteration to re-fetch the element
                continue

        # Add a short delay to prevent the loop from running too fast
        time.sleep(0.1)

except KeyboardInterrupt:
    # Gracefully close the browser when interrupted (Ctrl+C)
    print("Stopping script and closing browser.")
    driver.quit()
