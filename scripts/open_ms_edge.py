from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Initialize the Edge WebDriver using WebDriver Manager
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

# Open Google
driver.get("https://www.google.com")

# Print the page title
print("Page Title:", driver.title)

# Close the browser
driver.quit()
