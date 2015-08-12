from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.legco.gov.hk/general/english/counmtg/yr12-16/mtg_1415.htm")

response = driver.page_source

driver.close()
bshtml = BeautifulSoup(response, "html.parser")
print [href['href'] for href in filter(lambda x: re.search('xml', x['href']), bshtml.find_all(href=True))]
