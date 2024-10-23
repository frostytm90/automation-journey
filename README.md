# automation-journey

This repository is a learning journey to explore Selenium for web automation using Python. The project includes examples, scripts, and documentation aimed at mastering Selenium step-by-step.

## Project Structure
- **scripts/**: Python scripts for different Selenium tasks.
- **drivers/**: Optional: Web drivers for different browsers.
- **docs/**: Detailed documentation of the learning process.
- **README.md**: Overview and learning path.

## How to Set Up
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the dependencies:
    ```pip install -r requirements.txt```

## Getting Web Drivers
To use Selenium, you need to download the appropriate web driver for your browser.

### Supported Browsers:
1. **Chrome** - ChromeDriver (latest stable release)
2. **Firefox** - GeckoDriver (latest stable release)
3. **Edge** - EdgeDriver (latest stable release)
4. **Safari** (macOS only, pre-installed)

### Downloading a Web Driver
To download the latest stable release of a web driver, run the following command:
    ```python scripts/get_driver.py```

You will be prompted to select which driver you want to download. The driver will be placed in the `drivers/` folder.

## Learning Goals
- Understand web automation with Selenium.
- Automate browser actions like searching, interacting with elements, and handling alerts.
