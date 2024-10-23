from selenium import webdriver

# Setup the path to the ChromeDriver
driver.path = "./drivers/chromedriver" # Update your driver path or use environment variable

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(executable_path=driver.path)

# Open Google
driver.get("https://www.google.com")

# Print the page title
print("Page Title: " + driver.title)

# Close the browser
driver.quit()