#DO NOT REMOVE THIS
#Made by Merubokkusu | www.merubokkusu.com
#If you paid for this you got scammed.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from sys import platform
import time
import sys


email = sys.argv[1]
password = sys.argv[2]
inviteLink = sys.argv[3]
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("headless")
print("Starting Server Join")
if platform == "linux" or platform == "linux2":
    browser = webdriver.Chrome('resources/webdrivers/chromedriver-linux',chrome_options=chromeOptions)
elif platform == "darwin":
    browser = webdriver.Chrome('resources/webdrivers/chromedriver-mac',chrome_options=chromeOptions)
elif platform == "win32":
    browser = webdriver.Chrome('resources/webdrivers/chromedriver.exe',chrome_options=chromeOptions)

browser.get("https://discordapp.com/login")
element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "register-email")))
browser.find_element_by_id("register-email").send_keys(email)
print("Writing Email")
browser.find_element_by_id("register-password").send_keys(password)
print("Writing Password")
browser.find_element_by_css_selector("button.btn.btn-primary").click()
element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "guilds-add-inner")))
browser.execute_script('document.getElementsByTagName("body")[0].appendChild(document.getElementsByClassName("guilds-wrapper")[0])')
element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "app-mount")))
browser.execute_script('var el = document.querySelector( ".app-XZYfmp" ); el.parentNode.removeChild( el );')
mainmenu = browser.find_element_by_class_name("guilds-add-inner")
action=ActionChains(browser)
action.move_to_element(mainmenu).perform()
submenu = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "guilds-add-inner")))
print("Attempting to click") # Master hacking.
submenu.click()
print("Click success")
browser.find_element_by_css_selector("div.action.join > button.btn.btn-primary").click()
browser.execute_script("document.getElementsByClassName('link-container control-group')[0].style.top = 0;")
time.sleep(0.5);
browser.find_element_by_css_selector("div.link-container.control-group > input[type=\"text\"]").click()
browser.find_element_by_css_selector("div.link-container.control-group > input[type=\"text\"]").send_keys(inviteLink)
print("Writing invite link")
browser.find_element_by_css_selector("div.form-actions > button.btn.btn-primary").click()
print("Joined Server | Closing Script")
browser.quit()