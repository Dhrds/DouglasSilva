import pywhatkit
import pyautogui as a
import keyboard as k
import time as timesleep
import bd_lembrei as bd
import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("dhrds1996@gmail.com", "nxvkihjumvsthhto")
mensagem = "teste"

while True:
    bd.conexao()

    print(1)
    msg = bd.select_data('parametros_mensagem')
    print(msg,1)
    for i in msg :
        if  msg != '[]':
            print('ok')
            pywhatkit.sendwhatmsg_instantly ("+5537999775765", f"{mensagem}",10)
            timesleep.sleep(5)
            k.press_and_release('enter')
            server.sendmail(
             "dhrds1996@gmail.com",
             "guilhermesemusa@gmail.com",
             f"{mensagem}")
    timesleep.sleep (35)
    
    
    


# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.login("dhrds1996@gmail.com", "nxvkihjumvsthhto")
# server.sendmail(
#   "dhrds1996@gmail.com",
#   "destinatario@gmail.com",
#   f"{mensagem}")
# server.quit()