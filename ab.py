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
    if message.content.startswith('!AddEvent'):
        delims = 'title: ', ' time: ', ' place: '
        fields = regsplit(delims, message.content[10:])
        events.append(EventList(message.author, fields[1], fields[2], fields[3]))

    if message.content.startswith('!print'):
        for i in events:
            i.printDetails()
            print("-----------------")
    

def regsplit(delimitors, string, maxsplit=0):
    import re 
    regexPattern = '|'.join(map(re.escape, delimitors))
    return re.split(regexPattern, string, maxsplit)



client.run(f.readline())
