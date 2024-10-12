# simple_selenium_test.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Connect to Selenium server (localhost since GitHub Actions will use a service)
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open Google's homepage
    driver.get("https://www.google.com")

    # Get the page title
    page_title = driver.title

    # Check if the page title contains "Google"
    assert "Google" in page_title, "Google page title not found!"

    print("Test passed: Google homepage opened successfully.")

finally:
    # Close the browser
    driver.quit()
