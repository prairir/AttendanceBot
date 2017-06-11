import discord
import asyncio
from events import EventList 

client = discord.Client()

f = open('token.txt', 'r')

events = []

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------------------')

@client.event
async def on_message(message):
    if message.content.startswith('!addevent'):
        '''delims = 'title: ', ' time: ', ' place: '
        fields = regsplit(delims, message.content[10:])
        events.append(EventList(message.author, fields[1], fields[2], fields[3]))
        '''
        partParse(message.content[10:])
    if message.content.startswith('!print'):
        for i in events:
            i.printDetails()
            print("-----------------")
    
def partParse(mess):
    parts = mess.split(' ')
    argcount = 0
    place = 'b'
    time = 'x'
    title = 'd'
    for arg in parts:
        print('arg is {}'.format(arg))
        if arg == 'title:':
            argcount = 1
            continue

        elif arg == 'time:':
            argcount = 2
            continue

        elif arg == 'place:':
            argcount = 3
            continue

        if argcount == 1:
            title += ' ' + arg

        elif argcount == 2:
            time += ' ' + arg

        elif argcount == 3:
            place += ' ' + arg

    print(title)
    print(time)
    print(place)
def regsplit(delimitors, string, maxsplit=0):
    import re 
    regexPattern = '|'.join(map(re.escape, delimitors))
    return re.split(regexPattern, string, maxsplit)



client.run(f.readline())
