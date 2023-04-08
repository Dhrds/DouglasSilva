import pywhatkit
import pyautogui as a
import keyboard as k
import time
import bd_lembrei as bd
from datetime import date ,time as timehm

while True:
    bd.conexao
    check = bd.select_bd.select('verificacao')
    print(check)
    if check == [('N',)]:
        msg = bd.select_bd.select('parametros_mensagem')
        print(msg)
        ano =str(date.today.year)
        mes = str(date.today.month)
        dia = str(date.today.day)
        hora = str(timehm.hour)        
        minuto = str(timehm.minute)
        data = (ano,mes,dia,hora,minuto)
        print(data)
        for i in msg :
            if i[2] == data:
                pywhatkit.sendwhatmsg_instantly ("+5537999775765", "oi",10)
                time.sleep(5)
                k.press_and_release('enter')
    time.sleep (30)
    