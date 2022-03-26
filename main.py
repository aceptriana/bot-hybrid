#Bot Auto Absen Hybrid Uniku
#Acep Triana / Sistem Informasi
#Beta Version 1.0

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# Menjalankan Web Browser
browser  = webdriver.Chrome(ChromeDriverManager().install())


browser.get('https://hybrid.uniku.ac.id/login/index.php')

# Ganti Email dan Pw Lu

email = "20210910002@uniku.ac.id"
pw = "ayang166#"

browser.find_element_by_css_selector('#mm-0 > div.wrapper > section.our-log.bgc-fa > div > div > div > div > div.potentialidplist').click();
browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email)
browser.find_element_by_css_selector('#identifierNext > div > button > span').click();
time.sleep(10)
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(pw)
browser.find_element_by_css_selector('#passwordNext > div > button > span').click();
time.sleep(10)
browser.find_element_by_link_text('Profile')
