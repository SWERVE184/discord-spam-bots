#DO NOT REMOVE THIS
#Made by Merubokkusu | www.merubokkusu.com
#If you paid for this you got scammed.
import discord
import asyncio
import sys
import random
import os
import subprocess
sys.path.append("./.")
from config import *

client = discord.Client()
token = sys.argv[1]
spam_text = sys.argv[2]

@client.event
async def on_ready():
    print("Started Text Spam")
    while not client.is_closed:
        if os.path.exists('text.txt'):
            if textRandom == False:
                lines = open('text.txt').read().splitlines()
                spam_text = lines[0]
            else:
                lines = open('text.txt').read().splitlines()
                spam_text = random.choice(lines)
        print(spam_text)
        await client.send_message(discord.Object(id=DiscordChannel), spam_text)
        await asyncio.sleep(SpamSpeed) 

if '-:-' in token: 
    enp = token.split('-:-')
    p = subprocess.Popen(['python','bots/misc/joinServer.py',enp[0],enp[1],inviteLink],shell=True)
    p.wait()

    client.run(enp[0],enp[1], bot=False) 
else: 
    client.run(token, bot=False)