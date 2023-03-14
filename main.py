import telepot
from Chatbot import Chatbot

telegram = telepot.Bot("6118176276:AAHUIhXINEsywU1cHHhM8WkyYQLPLGLTGno")
bot = Chatbot("Lenina")

#bot.getUpdates()
#bot.sendMessage(2048202268,"Tudo otimo")

def recebendoMsg(msg):
    frase = bot.escuta(frase=msg["text"])
    resp = bot.pensa(frase)
    bot.fala(resp)
    chat_id = msg["chat"]["id"]
    telegram.sendMessage(chat_id, resp)
    
telegram.message_loop(recebendoMsg)

while True:
    pass