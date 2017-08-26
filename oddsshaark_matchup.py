import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup as soup

# Setup Selenium Chrome Web Driver
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

# Navigate in Chrome to specified page.
driver.get("http://www.oddsshark.com/ncaab/lsu-alabama-odds-february-18-2017-744793")

# Find the matchup list element using a css selector and click it.
link = driver.find_element_by_css_selector("li[id='react-tabs-0'").click()

# Wait for content to load
time.sleep(1)

# Get the current page source.
source = driver.page_source

# Parse into soup() the source of the page after the link is clicked and use "html.parser" as the Parser.
soupify = soup(source, 'html.parser')

dataList = []
for ultag in soupify.find_all('ul', {'class': 'base-list team-stats'}):
    print(ultag)
    for iltag in ultag.find_all('li'):
        dataList.append(iltag.get_text())
        
# We are done with the driver so quit.
driver.quit()
