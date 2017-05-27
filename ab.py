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
        events.append(EventList(message.author, message.content[9:],))

    if message.content.startswith('!print'):
        for i in events:
            i.printDetails()
            print("-----------------")



client.run(f.readline())
