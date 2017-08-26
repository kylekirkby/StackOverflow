import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import requests as req

# Setup Selenium Chrome Web Driver
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

# Navigate in Chrome to specified page.
driver.get("https://scholar.google.com/scholar?hl=en&q=Sustainability and the measurement of wealth: further reflections")

# Find "Cite" link by looking for anchors that contain "Cite" - second link selected "[1]"
link = driver.find_elements_by_xpath('//a[contains(text(), "' + "Cite" + '")]')[1]
# Click the link
link.click()

print("Waiting for page to load...")
time.sleep(2) # Sleep for 2 seconds

# Get Page source after waiting for 2 seconds of current page in Chrome
source = driver.page_source

# We are done with the driver so quit.
driver.quit()

# Use BeautifulSoup to parse the html source and use "html.parser" as the Parser
soupify = soup(source, 'html.parser')

# Find anchors with the class "gs_citi"
gs_citt = soupify.find('a',{"class":"gs_citi"})

# Get the href attribute of the first anchor found
href = gs_citt['href']

print("Fetching: ", href)

# Instantiate a new requests session
session = req.Session()

# Get the response object of href
content = session.get(href)

# Get the content and then decode() it.
bibtex_html = content.content.decode()

# Write the decoded data to a file named scholar.bib
with open("scholar.bib","w") as file:
    file.writelines(bibtex_html)
