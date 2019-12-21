# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# -*- encoding: utf-8 -*-

def enviador_correos(correos,tu_correo,contra,asunto):
	
	f= open('mensaje.txt', 'r')
	mensaje=f.read()
	f.close
	
	msg = MIMEMultipart()
	password = contra
	msg['From'] = tu_correo
	msg['To'] = correos
	msg['Subject'] = asunto
 
	msg.attach(MIMEText(mensaje, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com: 587')
	server.starttls()
	server.login(msg['From'], password)
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	server.quit()
	print ("Correo enviado satisfactoriamente a %s:" % (msg['To']))

archivo=open('direcciones.txt','r')
lines = archivo.readlines()
archivo.close()
tu_correo=input('\nIntroduce tu direccion de correo electronica (Tiene que ser de gmail): ')
contra=input('\nIntroduce la contraseña de tu correo: ')
asunto=input('\nIntroduce el asunto del correo: ')

for line in lines:
	
	enviador_correos(line,tu_correo,contra,asunto)




