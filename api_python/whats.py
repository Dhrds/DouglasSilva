import pywhatkit
import pyautogui as a
import keyboard as k
import time as timesleep
import bd_lembrei as bd
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

key = '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'


while True:
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
                message = Mail(
                from_email='dhrds1996@gmail.com',
                to_emails=email_env,
                subject=msg_env,
                html_content=f'<strong>{msg_env}</strong>')
                try:
                    sg = SendGridAPIClient(key)
                    
                    response = sg.send(message)
                    print(response.status_code)
                    print(response.body)
                    print(response.headers)
                except Exception as e:
                    print(e.message)   
                
            except:
                print('deu erro')
    timesleep.sleep (30)