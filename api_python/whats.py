import pywhatkit
import pyautogui as a
import keyboard as k
import time as timesleep
import bd_lembrei as bd
import datetime 

while True:
    bd.conexao()


    print(1)
    msg = bd.select_data('parametros_mensagem')
    print(msg,1)
    for i in msg :
        if  msg != '[]':
            print('ok')
            pywhatkit.sendwhatmsg_instantly ("+5537999775765", "oi",10)
            timesleep.sleep(5)
            k.press_and_release('enter')
    timesleep.sleep (35)
    