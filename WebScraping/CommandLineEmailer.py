#! python3
# CommandLineEmailer.py - Python Script to send an email

from selenium import webdriver
import sys

# Check if sys.args are empty
'''if len(sys.args) != 2:
    print('Not enough or too many args, closing this shit down')
    sys.exit(0)'''

# Open Chrome Browser with Selinum Webdriver and open up gmail
browser = webdriver.Chrome('fakepath')
browser.get('http://gmail.com')

# Input email and password and go to my account
email_elem = browser.find_element_by_id('Email')
email_elem.send_keys('fakemail')
email_elem.submit()
browser.implicitly_wait(10)
password_elem = browser.find_element_by_id('Passwd')
password_elem.send_keys('fakepass')
password_elem.submit()

try:
    browser.implicitly_wait(10)
    link_elem = browser.find_element_by_css_selector("T-I J-J5-Ji T-I-KE L3")
    link_elem.click()
except:
    print('Could not find proper link')