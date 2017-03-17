#! python3
# CommandLineEmailer.py - Python Script to send an email

from selenium import webdriver
import sys

# Check if sys.args are empty
if len(sys.argv) != 3:
    print('Not enough or too many args, closing this shit down')
    print(sys.argv)
    sys.exit(-1)

# Open Chrome Browser with Selinum Webdriver and open up gmail
# Downloaded chromedriver and placed inside Python folder
browser = webdriver.Chrome()
browser.get('http://gmail.com')

# Input email and submit
try:
    email_elem = browser.find_element_by_id('Email')
    email_elem.send_keys('fakemail')
    email_elem.submit()
except:
    print("Could not find proper email")
    sys.exit(1)

# Input password and go to my account
try:
    browser.implicitly_wait(10)
    password_elem = browser.find_element_by_id('Passwd')
    password_elem.send_keys('fakepass')
    password_elem.submit()
except:
    print("Could not find proper password")
    sys.exit(1)

# Pressing the compose button on the gmail page
try:
    browser.implicitly_wait(10)
    link_elem = browser.find_element_by_xpath("//div[text()='COMPOSE']")
    link_elem.click()
except:
    print('Could not find proper div')
    sys.exit(1)

# Inputs the email passed through system args into recipient section
try:
    browser.implicitly_wait(10)
    to_elem = browser.find_element_by_xpath("//textarea[@name='to']")
    to_elem.send_keys(sys.argv[1])
except:
    print('Could not find proper textarea')
    sys.exit(1)

# Inputs string into subject line
try:
    browser.implicitly_wait(10)
    subject_elem = browser.find_element_by_xpath("//input[@name='subjectbox']")
    subject_elem.send_keys('I\'m a meme')
except:
    print('Could not find proper input')
    sys.exit(1)

# Inputs a message from sys args into body section
try:
    browser.implicitly_wait(10)
    message_elem = browser.find_element_by_xpath("//div[@aria-label='Message Body']")
    message_elem.send_keys(sys.argv[2])
except:
    print('Could not find proper message box')
    sys.exit(1)

# Programatically clicks the send buttons and sends email
try:
    browser.implicitly_wait(10)
    send_elem = browser.find_element_by_xpath("//div[@aria-label='Send ‪(Ctrl-Enter)‬']")
    send_elem.click()
except:
    print('Could not find proper send button')
    sys.exit(1)

print("Finished!")
sys.exit(0)