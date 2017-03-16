from selenium import webdriver
browser = webdriver.Chrome('fakepath')
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

try:
    link_elem = browser.find_element_by_link_text('Read It Online')
    link_elem.click()
except:
    print('Could not find proper link')

browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('not_my_real_email@gmail.com')
emailElem.submit()
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('12345')
passwordElem.submit()

