from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re
import time


# Set up the Chrome driver
service = Service("YOUR_DRIVER_PATH")
driver = webdriver.Chrome(service=service)

#Ask URL and fileno from User
url = input("Enter URL: ")
iter = input("Enter Iteration: ")
filename = "linkedin_profiles" + iter +".csv"

def scrape_google_results():
    # Open the Google search results page
    driver.get(url)    # Wait for the search results to load
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.g')))

    # Create a list to store the scraped data
    scraped_data = []

    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        # Extract search results
        search_results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
        for result in search_results:
            try:
                # Extract the link to the LinkedIn profile
                profile_url = result.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                # Extract the visible text of the result
                profile_text = result.text

                # Debug: Print the profile text to understand what is being processed
                print("Profile Text:", profile_text)

                # Use regex to extract email addresses
                email_matches = re.findall(r'\b[A-Za-z0-9._%+-]+@gmail\.com\b', profile_text)
                if email_matches:
                    email = email_matches[0]  # Assume the first match is the desired email
                    # Extract the name if possible (assuming it's the first line in the text block)
                    name = profile_text.split('\n')[0]
                    scraped_data.append([name, email, profile_url])
            except Exception as e:
                print(f"Error occurred: {e}")

        # Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for new results to load
        time.sleep(5)  # Adjust time if needed

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # Break the loop if no new results are loaded
        last_height = new_height

    # Create a DataFrame from the scraped data
    df = pd.DataFrame(scraped_data, columns=['Name', 'Email', 'LinkedIn Profile URL'])

    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False, encoding='utf-8')

    print(f"Scraping completed. {len(scraped_data)} records saved to linkedin_profiles.csv")

# Call the scraping function
scrape_google_results()
# Close the browser
driver.quit()
