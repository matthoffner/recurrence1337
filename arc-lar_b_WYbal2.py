from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import time
f=open("arc-lar_b_20140716_000.csv","w")
browser = webdriver.Chrome("C:\Users\Matt\Downloads\chromedriver.exe")
browser.get("http://searcharchitects.state.wy.us/search.aspx")
#browser.find_element_by_css_selector("#ddlType > option:nth-child(2)").click()
browser.find_element_by_css_selector("#btnSearch").click()
#time.sleep(3)
#soup = BeautifulSoup(browser.page_source)


#links = browser.find_elements_by_css_selector("#gvLicensee > tbody > tr > td:nth-child(1) > a")
for a in browser.find_elements_by_css_selector("#gvLicensee > tbody > tr > td:nth-child(1) > a"):
    info = []
    info.append((a.get_attribute('href')))
    print ("\"" + "\"\n\"".join(info) + "\"\n")
    f.write("\"" + "\"\n\"".join(info) + "\"\n")
f.close()
#print soup.prettify()
#print soup.findAll('a', href=True)

"""for a in soup.findAll('a',href=True):
    if re.findall('ID=', a['href']):
        print a['href']
"""
"""for i in range(5597,6000):
    try:
        url = "http://searcharchitects.state.wy.us/Search.aspx?ID=%d"%i
        browser.get(url)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID,'form1')))
        c = browser.page_source
        soup = BeatifulSoup(c)
        nobr = soup.findAll("nobr")
        info = []
        info.append(nobr[8].text)
        info.append(nobr[9].text)
        info.append(nobr[10].text)
        info.append(nobr[11].text)
        info.append(nobr[13].text)
        info.append(nobr[15].text)
        info.append(nobr[16].text)
        info.append(nobr[17].text)
        info.append(nobr[18].text)
        print("\"" + "\",\"".join(info) + "\"\n")
        browser.back()
    except Exception, e:
        print str(e)"""
