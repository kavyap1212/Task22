from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to the chromedriver executable
s = Service('C:\\Users\\new\\OneDrive\\Documents\\Python Scripts\\Chromedriver\\chromedriver.exe')  # Update this to your path

# Initialize the WebDriver
driver = webdriver.Chrome(service=s, options=chrome_options)

# Open the Instagram profile page
driver.get("https://www.instagram.com/guviofficial/")

try:
    #Extract the number of followers
    followers_element = driver.find_element(By.CSS_SELECTOR, 'a[href$="/followers/"] > span')
    followers_count = followers_element.get_attribute("title")

    
    # Extract the number of following
    following_element = driver.find_element(By.CSS_SELECTOR, 'a[href$="/following/"] > span')
    following_count = following_element.get_attribute("title")

    # Print the results
    print(f"Followers: {followers_count}")
    print(f"Following: {following_count}")

finally:
    # Close the WebDriver
    driver.quit()