import random
import discord
from ungame_classes import *

games = UngameList()

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author != client.user:    
        return_message = games.command(message)
        if return_message:
            await client.send_message(message.channel, return_message)

client.run(take_token())