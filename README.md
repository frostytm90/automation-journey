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
I went ahead and created this automation script to open the Google Chrome Browser

- **Script**: `scripts/open_google_chrome.py`
  - The script opens up Google Chrome Browser and prints out the Page Title

**Example Code**:
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

## Example Automation: Cookie Clicker Bot

In addition to the simple browser actions and search automation scripts, I developed a more advanced automation script to play **Cookie Clicker**, an incremental game that requires clicking a large cookie to generate cookies and using them to buy upgrades.

- **Script**: `scripts/automate_cookie_clicker.py`  
  The script automates clicking the cookie in the game and purchasing upgrades to improve the cookie generation rate.

### How the Cookie Clicker Automation Works

This script is built using **Python** and **Selenium** to automate the gameplay for **Cookie Clicker**. Below, I provide a detailed explanation of what the script does and how it accomplishes the task of playing the game:

1. **Setting Up the WebDriver**:
    - The script uses `webdriver-manager` to automatically handle the ChromeDriver setup, ensuring compatibility between the Chrome browser and the driver:
    
    ```python
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    ```

2. **Navigating to the Game**:
    - The game is hosted at `https://orteil.dashnet.org/cookieclicker/`, and the script navigates to this URL:
    
    ```python
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    ```

3. **Language Selection**:
    - On the first load, the game requires the user to choose a language. The script selects English by locating and clicking the appropriate button:
    
    ```python
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Wait until the language selection element is available and select "English"
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
    )
    language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
    language.click()
    ```

4. **Clicking the Main Cookie**:
    - The script locates the main cookie element by its ID (`bigCookie`) and then clicks it continuously to accumulate cookies:
    
    ```python
    cookie = driver.find_element(By.ID, "bigCookie")
    while True:
        cookie.click()
    ```

5. **Purchasing Upgrades**:
    - The main goal is to increase the cookie production rate, which can be done by purchasing upgrades. The script monitors the cookie count and checks if enough cookies are available to buy the cheapest upgrade:
    
    ```python
    cookies_count = driver.find_element(By.ID, "cookies").text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))  # Remove commas and convert to integer

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

### Key Concepts and Techniques Used

1. **WebDriver Manager**:
   - **`webdriver_manager`** is used to automatically manage ChromeDriver. This eliminates the hassle of manually downloading and ensuring the driver version matches the installed Chrome version.

2. **Explicit Waits**:
   - The script uses explicit waits (`WebDriverWait`) to ensure elements are loaded before interacting with them. This is crucial for dealing with dynamic content and ensuring stable automation.

3. **Element Locators**:
   - **ID Locator**: Used to locate the main cookie button (`bigCookie`) and cookie count (`cookies`).
   - **XPath**: Used to locate the language selection button (`English`). XPath helps find elements with specific text.

4. **Automation Loop**:
   - The script runs an infinite loop to continuously click the main cookie and periodically check if there are enough cookies to buy upgrades. This is a typical pattern in automation where a specific task must be repeated indefinitely.

5. **Handling Dynamic Prices**:
   - The prices of products (upgrades) are retrieved dynamically. The script checks if the player has enough cookies and then clicks the appropriate product to purchase it.

### Running the Script

1. **Prerequisites**:
   - Install the required packages:
     ```bash
     pip install selenium webdriver-manager
     ```
   - Ensure you have Google Chrome installed.

2. **Execute the Script**:
   - Run the Python script:
     ```bash
     python scripts/automate_cookie_clicker.py
     ```

### Note
- **Infinite Loop**: The script runs indefinitely to click the cookie and purchase upgrades. You can stop the script manually by interrupting it (e.g., pressing `Ctrl+C` in the terminal).
- **Browser Control**: The script takes control of your Chrome browser. You can watch as it clicks the cookie and buys upgrades in real-time.

### Conclusion

This automation project is a fun way to practice Selenium skills, such as locating elements, handling waits, and interacting with dynamic content. By automating **Cookie Clicker**, I gained a deeper understanding of Selenium and how to automate repetitive tasks in a game environment.

Feel free to check out the script in the repository under `scripts/automate_cookie_clicker.py` and modify it to improve its efficiency or add more advanced features!

