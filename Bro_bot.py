import telebot # Librería de la API del bot.
 
from telebot import types # Tipos para la API del bot.
 
import time # Librería para hacer que el programa que controla el bot no se acabe.
 
 
# Aqui definiremos aparte del Token, por ejemplo los ids de los grupos y pondríamos grupo= -XXXXX 
 
  
TOKEN = '759493597:AAFXPvRlGtQ086wYyxcaqYG_FWz49FlXNVk' # Nuestro token del bot.
 

AYUDA = 'Puedes utilizar los siguientes comandos : \n\n/ayuda - Guia para utilizar el bot. \n/info - Informacion De interes \n/hola - Saludo del Bot \n/piensa3D - Informacion sobre Piensa3D \n\n'
 
 
GRUPO = -XXXXXX #Definimos que cuando pongamos la palabra grupo lo vincule con el Id del grupo donde nos encontremos.  Al meter el bot en un grupo, en la propia consola nos saldrá
 
 
 
 
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
 
############################################# 
 
#Listener
 
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
 
    for m in messages: # Por cada dato 'm' en el dato 'messages'
 
        cid = m.chat.id # El Cid es el identificador del chat los negativos son grupos y positivos los usuarios
 
        if cid > 0:
 
            mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text # Si 'cid' es positivo, usaremos 'm.chat.first_name' para el nombre.
 
        else:
 
            mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text # Si 'cid' es negativo, usaremos 'm.from_user.first_name' para el nombre.
 
        f = open( 'log.txt', 'a') # Abrimos nuestro fichero log en modo 'Añadir'.
 
        f.write(mensaje + "\n") # Escribimos la linea de log en el fichero.
 
        f.close() # Cerramos el fichero para que se guarde.
 
        print(mensaje) # Imprimimos el mensaje en la terminal, que nunca viene mal :) 
 
 
 
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.


AYUDA = 'Puedes utilizar los siguientes comandos : \n\n/ayuda - Guia para utilizar el bot. \n/info - Informacion De interes \n/hola - Saludo del Bot \n/piensa3D - Informacion sobre Piensa3D \n\n'
 
 
 
@bot.message_handler(commands=['ayuda']) # Indicamos que lo siguiente va a controlar el comando '/ayuda'
 
def command_ayuda(m): # Definimos una función que resuleva lo que necesitemos.
 
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
 
    bot.send_chat_action(cid, 'typing') # Enviando ...
 
    time.sleep(1) #La respuesta del bot tarda 1 segundo en ejecutarse
 
    bot.send_message( cid, AYUDA) # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.

    GRUPO = -XXXXXX
 
 
 
@bot.message_handler(commands=['info']) # Indicamos que lo siguiente va a controlar el comando '/info'
 
def command_info(m): # Definimos una función que resuleva lo que necesitemos.
 
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
 
    if cid == GRUPO:
 
        
 
            bot.send_message( GRUPO, 'mensaje A') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
 
    else :
 
            bot.send_message( cid, 'mensaje B')


@bot.message_handler(commands=['piensa3D']) # Indicamos que lo siguiente va a controlar el comando '/piensa3D'
 
def command_piensa3D(m): # Definimos una función que resuleva lo que necesitemos.
 
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
 
    Piensa3D = open('piensa3D.jpg', 'rb')
 
    xxx=open('xxx.mp3', 'rb')
 
    yyy=open('yyy.mp4', 'rb')
 
    zzz=open('zzz.jpg', 'rb')
 
    bot.send_sticker(cid, Piensa3D) # Con la función 'send_sticker()' del bot, enviamos al ID almacenado el texto que queremos.
 
    bot.send_audio(cid, xxx)
 
    bot.send_video(cid, yyy)
 
    bot.send_photo(cid, zzz)
 
    bot.send_message(cid, "hola")
 
    piensa3D.close()
 
    xxx.close()
 
    yyy.close()
 
    zzz.close()

@bot.message_handler(func=lambda message: message.text == "hola")
 
def command_text_hola(m):
 
    time.sleep(1)
 
    bot.send_message(m.chat.id, "Hola a ti tambien")

bot.polling(none_stop=True)