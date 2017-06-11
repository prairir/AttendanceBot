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
        fields = partParse(message.content[10:])
        events.append(EventList(message.author, fields[0], fields[1], fields[2]))

    if message.content.startswith('!print'):
        for i in events:
            i.printDetails()
            print("-----------------")
    
def partParse(mess):
    parts = mess.split(' ')
    argcount = 0
    place = ''
    time = ''
    title = ''
    for arg in parts:
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

    atributes = [title, time, place]
    return atributes
client.run(f.readline())
