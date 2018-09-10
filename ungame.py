import random
import discord
from ungame_classes import *

END_MESSAGE = "This is the end of the game.\nThank you for playing!"
phrase = {"join":"join", "next":"next"}

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



@client.event
async def on_message(message):

    if message.content.startswith("/"):
        cmd = message[1:].split(" ")

        if cmd[0] == "ungame":

            if cmd[1] == "phrase":
                if cmd[2] == "join":
                    join_phrase = cmd[3]
                elif cmd[2] == "next":
                    next_phrase = cmd[3]

            elif cmd[1] == "open": # ここからgame開始


            elif cmd[1] == "start":
                deck = Deck(take_questions())

                while True:
                    if deck.questions == []:
                        await client.send_message(message.channel, END_MESSAGE)
                        break

                    elif message.content == start_message:
                        await client.send_message(message.channel, deck.draw())

            elif cmd[1] == "end":

                await client.send_message(message.channel, END_MESSAGE)



        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)

client.run(take_token())