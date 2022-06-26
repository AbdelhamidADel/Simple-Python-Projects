import pywhatkit
from datetime import datetime
import pyautogui
now = datetime.now()

chour = now.strftime("%H")
mobile = input('Enter Mobile No of Receiver : ')
message = input('Enter Message you wanna send : ')
hour = int(input('Enter hour : '))
minute = int(input('Enter minute : '))
pyautogui.press("enter")

pywhatkit.sendwhatmsg(mobile,message,hour,minute)