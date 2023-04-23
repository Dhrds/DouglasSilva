import pywhatkit
import pyautogui as a
import keyboard as k
import time as timesleep
import bd_lembrei as bd
import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("douglas.silvateste01@gmail.com", "rigaqztdnmozfjmd")

while True:
    bd.conexao()

    print(1)
    msg = bd.select_data('parametros_mensagem')
    print(msg,1)
    for i in msg :
        if  msg != '[]':
            try:
                print(type(msg))
                user = i[1]
                id = i[6]
                msg_env = i[2]
                num = '+'+i[3]
                email_env = i[4]
                env = i[5]
                print(user,id,msg_env,num,email_env,env)
                info = bd.select_usuario(user)
                print(2)
                pywhatkit.sendwhatmsg_instantly (num, f"{msg_env}",10)
                timesleep.sleep(10)
                k.press_and_release('enter')
                bd.alterar(id)
                server.sendmail(
                "douglas.silvateste01@gmail.com",
                email_env,
                f"{msg_env}")
                server.quit()
            except:
                print('deu erro')
    timesleep.sleep (5)
    
    
    


# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.login("dhrds1996@gmail.com", "")

# server.sendmail(
#   "dhrds1996@gmail.com",
#   "destinatario@gmail.com",
#   f"{mensagem}")
# server.quit()