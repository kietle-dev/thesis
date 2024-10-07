import time
from selenium import webdriver
from PIL import Image
import schedule

def capture_website_screenshot(url, output_file):
    # Setup WebDriver (Make sure you have the appropriate WebDriver installed, e.g., chromedriver)
    driver = webdriver.Chrome()  # You can also use other drivers like Firefox, Safari, etc.
    
    # Open the website
    driver.get(url)
    
    # Take screenshot
    screenshot = driver.get_screenshot_as_png()
    
    # Save the screenshot
    with open(output_file, 'wb') as file:
        file.write(screenshot)
    
    # Close the driver
    driver.quit()

def job():
    url = "https://www.google.com/"  # Replace with the desired URL
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_file = f"screenshots/screenshot_{timestamp}.png" # Replace with the desired output file path
    capture_website_screenshot(url, output_file)

if __name__ == "__main__":
    # Schedule the job every hour
    schedule.every(1).minute.do(job)

    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(1)