from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import EdgeDriverManager

# Initialize the Chrome WebDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Google site
driver.get("https://www.google.com")

# Print the page title
print("Page Title:", driver.title)

# Close the browser
driver.quit()
