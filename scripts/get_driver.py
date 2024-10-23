import os
import requests
import zipfile
import platform

def download_driver(url, driver_name, output_folder="./drivers"):
    local_zip = f"{driver_name}.zip"

    # Download the driver
    print(f"Downloading {driver_name}...")
    response = requests.get(url)
    with open(local_zip, 'wb') as file:
        file.write(response.content)

    # Extract the driver
    print(f"Extracting {driver_name}...")
    with zipfile.ZipFile(local_zip, 'r') as zip_ref:
        zip_ref.extractall(output_folder)

    # Clean up
    os.remove(local_zip)
    print(f"{driver_name} downloaded and extracted to {output_folder}")

def download_chromedriver():
    # Get the latest ChromeDriver version
    version_url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
    response = requests.get(version_url)
    latest_version = response.text.strip()

    system_os = platform.system()
    if system_os == "Windows":
        url = f"https://chromedriver.storage.googleapis.com/{latest_version}/chromedriver_win32.zip"
    elif system_os == "Linux":
        url = f"https://chromedriver.storage.googleapis.com/{latest_version}/chromedriver_linux64.zip"
    elif system_os == "Darwin":
        url = f"https://chromedriver.storage.googleapis.com/{latest_version}/chromedriver_mac64.zip"
    else:
        raise Exception("Unsupported operating system")
    download_driver(url, "chromedriver")

def download_geckodriver():
    # Get the latest GeckoDriver version from GitHub API
    api_url = "https://api.github.com/repos/mozilla/geckodriver/releases/latest"
    response = requests.get(api_url)
    latest_release = response.json()
    latest_version_tag = latest_release["tag_name"]

    system_os = platform.system()
    if system_os == "Windows":
        url = f"https://github.com/mozilla/geckodriver/releases/download/{latest_version_tag}/geckodriver-{latest_version_tag}-win64.zip"
    elif system_os == "Linux":
        url = f"https://github.com/mozilla/geckodriver/releases/download/{latest_version_tag}/geckodriver-{latest_version_tag}-linux64.tar.gz"
    elif system_os == "Darwin":
        url = f"https://github.com/mozilla/geckodriver/releases/download/{latest_version_tag}/geckodriver-{latest_version_tag}-macos.tar.gz"
    else:
        raise Exception("Unsupported operating system")
    download_driver(url, "geckodriver")

def download_edgedriver():
    # Get the latest EdgeDriver version
    version_url = "https://msedgedriver.azureedge.net/LATEST_STABLE"
    response = requests.get(version_url)
    latest_version = response.text.strip()

    system_os = platform.system()
    if system_os == "Windows":
        url = f"https://msedgedriver.azureedge.net/{latest_version}/edgedriver_win64.zip"
    elif system_os == "Linux":
        url = f"https://msedgedriver.azureedge.net/{latest_version}/edgedriver_linux64.zip"
    elif system_os == "Darwin":
        url = f"https://msedgedriver.azureedge.net/{latest_version}/edgedriver_mac64.zip"
    else:
        raise Exception("Unsupported operating system")
    download_driver(url, "edgedriver")

# SafariDriver is pre-installed on macOS systems

def main():
    print("Which web driver would you like to download?")
    print("1: ChromeDriver")
    print("2: GeckoDriver (Firefox)")
    print("3: EdgeDriver")
    print("4: SafariDriver (macOS only, pre-installed)")
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        download_chromedriver()
    elif choice == '2':
        download_geckodriver()
    elif choice == '3':
        download_edgedriver()
    elif choice == '4' and platform.system() == "Darwin":
        print("SafariDriver is already installed on macOS.")
    else:
        print("Invalid choice or unsupported system.")

if __name__ == "__main__":
    main()
