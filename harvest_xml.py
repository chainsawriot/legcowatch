from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

driver = webdriver.Firefox()
driver.get(sys.argv[1])

response = driver.page_source

driver.close()
bshtml = BeautifulSoup(response, "html.parser")
for h in [href['href'] for href in filter(lambda x: re.search('xml', x['href']), bshtml.find_all(href=True))]:
    print 'http://legco.gov.hk' + h

