from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import pyautogui

usr=input('Enter Email Id:')
pwd=input('Enter Password:')

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/accounts/login/')
print ("Opened instagram")
sleep(1)

username_box = driver.find_element_by_name('username')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)

password_box = driver.find_element_by_name('password')
password_box.send_keys(pwd)
print ("Password entered")
sleep(2)
pyautogui.press("enter")

print ("Done")
input('Press anything to quit')
driver.quit()
print("Finished")