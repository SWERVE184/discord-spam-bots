import discord
import asyncio
import sys
import random
import os
sys.path.append("./.")
from config import *

client = discord.Client()
token = sys.argv[1]
spam_text = sys.argv[2]

@client.event
async def on_ready():
    print("Started Text Spam")
    while not client.is_closed:
        if textRandom == False:
            lines = open('text.txt').read().splitlines()
            spam_text = lines[0]
        else:
            lines = open('text.txt').read().splitlines()
            spam_text = random.choice(lines)
        print(spam_text)
        await client.send_message(discord.Object(id=DiscordChannel), spam_text)
        await asyncio.sleep(SpamSpeed) 

client.run(token, bot=False)

        




