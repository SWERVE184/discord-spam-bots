import urllib.request
import discord
import asyncio
import sys
from bs4 import BeautifulSoup
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
                UserList = server.members
        else:
            UserList = server.members

    for member in list(UserList):
        if(member.id != client.user.id):
            userNames = open('dm_spam_insult.txt');
            text = userNames.read().strip().split()
            if member.id in text: 
                print(member.name + ' was already messaged')
            else:
                try:
                    print('Sent message to '+ member.name)
                    file = open('dm_spam_insult.txt','a')
                    file.writelines(member.id + '\n')
                    file.close()
                    html = urllib.request.urlopen("https://insult.mattbas.org/api/insult.html").read()
                    soup = BeautifulSoup(html,"html.parser")
                    insult_text = soup.find('h1')
                    print(insult_text.text)
                    await client.send_message(member, insult_text.text)
                    for remaining in range(31, 0, -1):# Changes how fast the messages are sent. (Discord has a 10 minute cool down for every 10 users)
                        sys.stdout.write("\r")
                        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                        sys.stdout.flush()
                        await asyncio.sleep(1)
                    sys.stdout.write("\rComplete!                    \n")
                except Exception:
                    print('Something went wrong (;3;) relaunching...') 
    
client.run(token,bot=False)
