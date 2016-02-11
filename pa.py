import telepot, time
from nltk.chat.iesha import iesha_chatbot

is_chatting = False

def handle(msg):
    global is_chatting
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Got command: %s' % command
    
    if command == '/hello':
        bot.sendMessage(chat_id, "Hello, how are you?")
    if command == '/chat':
        is_chatting = True
        bot.sendMessage(chat_id, 'Hi I am Iesha. Who are You?')
    elif command == '/stopchat':
        is_chatting = False
        bot.sendMessage(chat_id, 'Bye Bye. take care!')
    elif not command.startswith('/') and is_chatting:
        bot.sendMessage(chat_id, iesha_chatbot.respond(command))
    else:
        pass


# Insert API
bot = telepot.Bot('API your bot')
bot.notifyOnMessage(handle)
while 1:
    time.sleep(10)