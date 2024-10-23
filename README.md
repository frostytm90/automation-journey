# automation-journey

This repository serves as my learning journey to explore Selenium for web automation using Python. The project includes examples, scripts, and documentation aimed at mastering Selenium step-by-step.

## Learning Goals
- Understand web automation with Selenium.
- Automate browser actions like searching, interacting with elements, and handling alerts.
- Learn how to use different element locators in Selenium.
- Practice handling waits and dealing with dynamic content.

## Project Structure
- **scripts/**: Python scripts for different Selenium tasks.
- **drivers/**: Optional: Web drivers for different browsers.
- **docs/**: Detailed documentation of the learning process.
- **README.md**: Overview and learning path.

## How to Set Up
1. Clone the repository.
    ```bash
    git clone https://github.com/frostytm90/automation-journey.git
    cd automation-journey
    ```
2. Create and activate a virtual environment.
    ```bash
    python -m venv selenium-env
    ```
   - **Windows**: `selenium-env\Scripts\activate`
   - **Linux/macOS**: `source selenium-env/bin/activate`
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Getting Web Drivers
To use Selenium, WebDriver Manager can be used to automatically download the appropriate web driver for your browser.

### Supported Browsers:
1. **Chrome** - ChromeDriver (latest stable release)
2. **Firefox** - GeckoDriver (latest stable release)
3. **Edge** - EdgeDriver (latest stable release)
4. **Safari** (macOS only, pre-installed)

## Example Automation: Open Google Chrome Browser
I created the following example to automate the open of Google Chrome

- **Script**: `scripts/open_google_chrome.py`
    - The script will open the Google Chrome browser and print out the Page title.

**Example Code**
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome WebDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Google site
driver.get("https://www.google.com")

# Print the page title
print("Page Title:", driver.title)

# Close the browser
driver.quit()
```

## Example Automation: Google Search
I've enhanced the example script to include automation example like performing a Google search.

- **Script**: `scripts/search_google_chrome.py`
  - The script opens Google, searches for the term "Selenium Python", and prints the title of the results page.

**Example Code**:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome WebDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Find the search bar using its name attribute value
search_box = driver.find_element(By.NAME, "q")

# Send a search term to the search box and press enter
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Wait for the results to load and print the title
driver.implicitly_wait(5)
print("Page Title After Search:", driver.title)

# Close the browser
driver.quit()
