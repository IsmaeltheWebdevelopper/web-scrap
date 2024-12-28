import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service('/Users/ismadiane/Desktop/Year up/MOD 3/PYTHON/week 17/project 3/chromedriver')


driver = webdriver.Chrome(service=service)


driver.get('https://www.yearupalumni.org/s/1841/interior.aspx?sid=1841&gid=2&pgid=440')

# Extract the page source
content = driver.page_source

# Parse the content with BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Quit the WebDriver
driver.quit()

# Extract relevant elements
results = []
for element in soup.findAll(attrs={'class': 'title'}):  # Adjust 'class' or other attributes as needed
    name = element.find('a')
    if name and name.text.strip() not in results:
        results.append(name.text.strip())

# Create a DataFrame
df = pd.DataFrame({'Names': results})

# Save to a CSV file
df.to_csv('names.csv', index=False, encoding='utf-8')

print("Scraping completed. Data saved to 'names.csv'.")
