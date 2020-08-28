from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
from bs4 import BeautifulSoup

capabilities = webdriver.DesiredCapabilities().FIREFOX                  
capabilities["marionette"] = True      

binary = FirefoxBinary('/usr/bin/firefox-esr')   
driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities, executable_path='/home/koblitz/Documents/gecko/geckodriver')
driver.maximize_window()


def login():
	driver.get("https://www.facebook.com")

	em = driver.find_element_by_id('email')
	em.send_keys('koblitz2020.3@gmail.com')
	sn =driver.find_element_by_id('pass')
	sn.send_keys('Super_Amigos')

	lclick = driver.find_element_by_id('u_0_b')
	lclick.click()

driver.get("https://www.facebook.com/anaclara.silvadamotta.5?eid=ARCnTWu_ZQRCw3O7ADPLsFuGuJZWWptUY331URGOcbARRStEdmBT2_YaaJdcESKNVjWzBkJG2gLc9mb7&timeline_context_item_type=intro_card_relationship&timeline_context_item_source=100004245309827")

def tere(addr):
	driver.get(addr)
	lo = driver.page_source
	soup = BeautifulSoup(lo, 'html.parser')
	loc =str(soup.findAll("a", { "class" : "profileLink" }))
	ls = loc.split(">")
	if "Teresópolis" in ls[1]:
		return 1
	elif "Teresópolis" in ls[3]:
		return 1
	elif "Teresópolis" in ls[5]:
		return 1
	elif "Teresópolis" in ls[7]:
		return 1
	elif "Teresópolis" in ls[9]:
		return 1
	else:
		return 0


def comum(addr):
	driver.get(addr)
	lo1 =driver.page_source
	soup2 =BeautifulSoup(lo1, 'html.parser')
	for link in soup2.findAll("a", { "class" : "_6-6" }):
		am = link.get('href')
		if "friends" in am: 
			driver.get(am)
			lo2 = driver.page_source
			soup3 = BeautifulSoup(lo2, 'html.parser')
			cc =str(soup3.findAll("ul", { "class" : "uiList _262m _4kg" }))
			if "Koblitz" in cc:
				return 2
			else:
				return 3

def amigoadd(addr):
	driver.get(addr)
	addbutton = driver.find_element_by_id("u_ps_0_0_2")
	addbutton.click()

def getname(addr):
	driver.get(addr)
	lo3 = driver.page_source
	soup4 = BeautifulSoup(lo3, 'html.parser')
	for nb in soup4.findAll("a", { "class" : "_2nlw _2nlv" }): 
		nb1 = str(nb) 
		nb2 = nb1.split('>')[1]
		print(nb2)


