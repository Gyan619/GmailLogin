from selenium import webdriver
from time import sleep

usr = input('Enter your email id:')
pwd = input('Enter your password:')

googleDriver = webdriver.Chrome()
googleDriver.get('https://www.google.com/intl/en-GB/gmail/about/#')
print('Gmail home page opened')
main_page = googleDriver.current_window_handle
# googleDriver.implicitly_wait(5)
#actions = webdriver.ActionChains(googleDriver)


signing_box = googleDriver.find_element_by_xpath(
    "//li[@class='h-c-header__nav-li g-mail-nav-links']//a[contains(text(),'Sign in') and @ga-event-action='sign in' and @class='h-c-header__nav-li-link ']")

current_url = googleDriver.current_url
print(current_url)
signing_box.click()
sleep(3)
login_page = googleDriver.current_window_handle
for handle in googleDriver.window_handles:
    if handle != main_page:
        login_page = handle

googleDriver.switch_to.window(login_page)

email_box = googleDriver.find_element_by_xpath("//input[@type='email']")
email_box.clear()
email_box.send_keys(usr)

print('Email id entered')
sleep(2)

next_click = googleDriver.find_element_by_xpath(
    "//span[@class='RveJvd snByac']")
next_click.click()
sleep(3)

# googleDriver.switch_to.default_window()
#pwd_box = googleDriver.switch_to.frame(googleDriver.find_element_by_xpath("//input[@type='password']"))

pwd_box = googleDriver.find_element_by_xpath("//input[@type='password']")
sleep(3)
pwd_box.clear()
pwd_box.send_keys(pwd)

print('password entered')
sleep(2)

login_box = googleDriver.find_element_by_xpath("//span[text()='Next']")
login_box.click()
print('Done')
