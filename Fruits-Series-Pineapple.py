from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl

# Replace with your email and password
email = "datapanel57@gmail.com"
password = "bigbang.ai"

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

# Start a Chrome web browser
driver = webdriver.Chrome(options=chrome_options)

# Open the Gmail sign-in page
driver.get("https://accounts.google.com")

# Find the email input element and type your email
email_input = driver.find_element(By.ID, "identifierId")
email_input.send_keys(email)
email_input.send_keys(Keys.RETURN)

# Wait for a few seconds
time.sleep(2)

# Find the password input element by its CSS selector and wait for it to be interactable
password_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="password"]'))
)
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

# Wait for a few seconds to log in
time.sleep(5)

# Navigate to the Gmail inbox
driver.get("https://mail.google.com")

# Wait for the inbox to load (adjust the timeout as needed)
WebDriverWait(driver, 20).until(EC.title_contains("Inbox"))

# Find the element containing the number of emails
emails_count_element = driver.find_element(By.CSS_SELECTOR, '.bsU')
emails_count = emails_count_element.text
print("Number of emails in the inbox:", emails_count)

# Save the count to an Excel file
excel_file = "email_count.xlsx"
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet["A1"] = "Email Count"
sheet["B1"] = emails_count

workbook.save(excel_file)

# Add further actions or navigate to other pages as needed.

# Close the browser
#driver.quit()
