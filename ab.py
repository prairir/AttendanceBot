import discord
import asyncio
import sqlite3

db = sqlite3.connect('data/base.db')
cursor = db.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS events(author TEXT, title TEXT, time TEXT, place TEXT)''')
cursor.execute(''' CREATE TABLE IF NOT EXISTS going(author TEXT, title TEXT)''')

client = discord.Client()

f = open('token.txt', 'r')


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
        title, time, place = fields
        cursor.execute(''' INSERT INTO events(author, title, time, place) VALUES(?, ?, ?, ?)''',
        (str(message.author), title, time, place))
        db.commit()

    if message.content.startswith('!print'):
        cursor.execute(''' SELECT * FROM events''')
        db.commit()
        for row in cursor.fetchall():
            print(row)

    if message.content.startswith('!cleanevent'):
        cursor.execute(''' DELETE FROM events ''')
        db.commit()
        cursor.execute(''' VACUUM''')
        db.commit()
        print('all clean')

    if message.content.startswith('!cleangoing'):
        cursor.execute(''' DELETE FROM going ''')
        db.commit()
        cursor.execute(''' VACUUM''')
        db.commit()
        print('all clean')



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
