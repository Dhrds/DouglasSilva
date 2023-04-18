import schedule
import time
import datetime
import pywhatkit
import pyautogui as a
import keyboard as k

def envio():
        pywhatkit.sendwhatmsg_instantly ("+5537999775765", "oi",10)
        time.sleep(5)
        k.press_and_release('enter')


def diario():
    schedule.every().days.do(envio()) 
        
        
        
diario()