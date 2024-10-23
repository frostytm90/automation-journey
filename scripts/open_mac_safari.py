from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Initialize the Firefox WebDriver using WebDriver Manager
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# Open Google
driver.get("https://www.google.com")

# Print the page title
print("Page Title:", driver.title)

# Close the browser
driver.quit()
