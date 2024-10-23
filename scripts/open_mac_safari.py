from selenium import webdriver

# This only works for macOS platforms.

# Initialize the Safari WebDriver (SafariDriver is pre-installed on macOS)
driver = webdriver.Safari()

# Open Google
driver.get("https://www.google.com")

# Print the page title
print("Page Title:", driver.title)

# Close the browser
driver.quit()

