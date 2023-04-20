import pywhatkit
import pyautogui as a
import keyboard as k
import time as timesleep
import bd_lembrei as bd
import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("douglas.silvateste01@gmail.com", "jmtwbzwroentjugsl")
server.login("dhrds1996@gmail.com", "")
mensagem = "teste"

while True:
    bd.conexao()

    print(1)
    msg = bd.select_data('parametros_mensagem')
    print(msg,1)
    for i in msg :
        if  msg != '[]':
            try:
                print(type(msg))
                user = msg[0][1]
                print(user)
                info = bd.select_usuario(user)
                email = info[0][1]
                tel = info[0][0]
                pywhatkit.sendwhatmsg_instantly (tel, f"{mensagem}",10)
                timesleep.sleep(5)
                k.press_and_release('enter')
                server.sendmail(
                "douglas.silvateste01@gmail.com",
                email,
                f"{mensagem}")
                server.quit()
            except:
                print('deu erro')
    timesleep.sleep (35)
    
    
    


# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.login("dhrds1996@gmail.com", "")

# server.sendmail(
#   "dhrds1996@gmail.com",
#   "destinatario@gmail.com",
#   f"{mensagem}")
# server.quit()