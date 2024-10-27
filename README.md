# Selenium Automation Journey

This repository documents my journey in learning Selenium for web automation using Python. You'll find scripts, examples, and some notes that helped me master Selenium step by step.

## Learning Goals
- Understand the basics of web automation with Selenium.
- Automate browser actions like searching, interacting with elements, and handling alerts.
- Learn how to use different element locators in Selenium.
- Practice handling waits and dynamic content.

## Project Structure
- **scripts/**: Python scripts for various Selenium tasks.
- **drivers/**: Optional web drivers for different browsers.
- **docs/**: Documentation of my learning journey.
- **README.md**: Overview and learning path (this file!).

## Setting Up
1. Clone the repository:
    ```bash
    git clone https://github.com/frostytm90/automation-journey.git
    cd automation-journey
    ```
2. Create and activate a virtual environment:
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
To use Selenium, you'll need the appropriate web driver for your browser. I use **WebDriver Manager** to automatically download the required driver.

### Supported Browsers
- **Chrome** - ChromeDriver (latest stable release)
- **Firefox** - GeckoDriver (latest stable release)
- **Edge** - EdgeDriver (latest stable release)
- **Safari** - Pre-installed on macOS

## Example Automation Scripts

### 1. Opening Google Chrome
A simple script to open Google Chrome and print the page title.

- **Script**: `scripts/open_google_chrome.py`

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Print the page title
print("Page Title:", driver.title)

# Close the browser
driver.quit()
```

### 2. Google Search Automation
An enhanced script that opens Google and searches for "Selenium Python".

- **Script**: `scripts/search_google_chrome.py`

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Find the search bar and search for "Selenium Python"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Wait for results and print the title
driver.implicitly_wait(5)
print("Page Title After Search:", driver.title)

# Close the browser
driver.quit()
```

### 3. Automating Cookie Clicker Game
A more advanced script to automate playing **Cookie Clicker** — clicking the cookie and buying upgrades.

- **Script**: `scripts/automate_cookie_clicker.py`

#### How It Works

1. **Setting Up the WebDriver**
   - Uses `webdriver-manager` to automatically set up ChromeDriver.

   ```python
   from selenium import webdriver
   from selenium.webdriver.chrome.service import Service
   from webdriver_manager.chrome import ChromeDriverManager

   service = Service(ChromeDriverManager().install())
   driver = webdriver.Chrome(service=service)
   ```

2. **Navigating to Cookie Clicker**
   - The game is hosted at `https://orteil.dashnet.org/cookieclicker/`.

   ```python
   driver.get("https://orteil.dashnet.org/cookieclicker/")
   ```

3. **Language Selection**
   - The script selects **English** at the start.

   ```python
   from selenium.webdriver.common.by import By
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC

   WebDriverWait(driver, 5).until(
       EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
   )
   language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
   language.click()
   ```

4. **Clicking the Big Cookie**
   - Continuously clicks the main cookie (`bigCookie`).

   ```python
   cookie = driver.find_element(By.ID, "bigCookie")
   while True:
       cookie.click()
   ```

5. **Buying Upgrades**
   - Checks for upgrades and buys them when enough cookies are available.

   ```python
   cookies_count = driver.find_element(By.ID, "cookies").text.split(" ")[0]
   cookies_count = int(cookies_count.replace(",", ""))

   for i in range(4):
       product_price = driver.find_element(By.ID, "productPrice" + str(i)).text.replace(",", "")

       if not product_price.isdigit():
           continue

       product_price = int(product_price)
       
       if cookies_count >= product_price:
           product = driver.find_element(By.ID, "product" + str(i))
           product.click()
           break
   ```

### Running the Script

1. **Install the Requirements**
   ```bash
   pip install selenium webdriver-manager
   ```

2. **Run the Script**
   ```bash
   python scripts/automate_cookie_clicker.py
   ```

### Notes
- The script runs in an infinite loop, so you'll need to stop it manually (e.g., `Ctrl+C` in the terminal).
- The browser is fully controlled by the script, so you can watch the automation in action.
