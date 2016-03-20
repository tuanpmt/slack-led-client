from slackbot.bot import respond_to
from slackbot.bot import listen_to

from tinydb import TinyDB, where, Query
import re
import json

@respond_to('write (.*)', re.IGNORECASE)
def write(message, args):
    # message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    #message.react('+1')
    db = TinyDB('db.json')
    db.insert({'value': args});
    print args
    db.close()
    
@respond_to('read', re.IGNORECASE)
def read(message):
    db = TinyDB('db.json')
    message.reply('Foo <!everyone> bar http://test.com')
    db.close()

@respond_to('github', re.IGNORECASE)
def github(message):
    attachments = [
    {
        'fallback': 'Fallback text',
        'author_name': 'Author',
        'author_link': 'http://www.github.com',
        'text': 'Some text',
        'color': '#59afe1'
    }]
    message.send_webapi('', json.dumps(attachments))

@listen_to('Can someone help me?')
def help(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('Yes, I can!')