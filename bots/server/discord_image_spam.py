import discord
import asyncio
import random
import os
import sys
sys.path.append("./.")
from config import *

client = discord.Client()
token = sys.argv[1]
UserList = []

@client.event
async def on_ready():
    for server in client.servers:
        if ScanAllServers == False:
            if(server.id == DiscordServer):
                for member in server.members:
                    if(member.id != client.user.id):
                        UserList.append(member)
        else:
            for member in server.members:
                if(member.id != client.user.id):
                    UserList.append(member)

    for member in UserList:
        userNames = open('dm_spam_image.txt');
        text = userNames.read().strip().split()
        if member.id in text: 
            print(member.name + ' was already messaged')
        else:
            try:
                UpImage = random.choice(os.listdir(DirPictures)) 
                await client.send_file(member, DirPictures + UpImage)
                print('Sent '+ UpImage + ' to '+ member.name)
                file = open('dm_spam_image.txt','a')
                file.writelines(member.id + '\n')
                file.close()
                for remaining in range(31, 0, -1):# Changes how fast the messages are sent. (Discord has a 10 minute cool down for every 10 users)
                    sys.stdout.write("\r")
                    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                    sys.stdout.flush()
                    await asyncio.sleep(1)
                sys.stdout.write("\rComplete!                    \n")
            except Exception:
                print('Something went wrong (;3;) relaunching...') 

client.run(token, bot=False)
