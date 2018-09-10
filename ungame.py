import random
import discord
from ungame_classes import *

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("/ungame"):
        commands = message[7:].split(" ")

    if commands[0] == "phrase":
        if commands[1] == "join":

        elif commands[1] == "next":

    elif commands[0] == "open":


    elif commands[0] == "end" or #カードがなくなった時:



        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)

client.run(take_token())