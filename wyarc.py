from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import codecs
import re
f=codecs.open("arc-lar_i_20140717_000.csv","w","utf-8")
s = requests.session()
#browser = webdriver.Chrome()
for line in codecs.open("arc-lar-WY.csv"):
    try:
        asdf = "%s" %line
        link = asdf.replace("\"","")
        source = s.get(link)
        #c = browser.page_source
        soup = BeautifulSoup(source.content)
        nobr = soup.findAll("nobr")
        info = []
        info.append(nobr[8].text)
        #info.append(nobr[9].text)
        info.append(nobr[10].text)
        info.append(nobr[11].text)
        info.append(nobr[13].text)
        info.append(nobr[15].text)
        info.append(nobr[16].text)
        info.append(nobr[17].text)
        info.append(nobr[18].text)
        print("\"" + "\",\"".join(info) + "\"\n")
        f.write("\"" + "\",\"".join(info) + "\"\n")
        #print browser.current_url
    except Exception, e:
        print str(e)
        
