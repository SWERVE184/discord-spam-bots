#DO NOT REMOVE THIS
#Made by Merubokkusu | www.merubokkusu.com
#If you paid for this you got scammed.
import urllib.request
import discord
import asyncio
import sys
import subprocess
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
                UserList = list(server.members)
        else:
            UserList = list(server.members)
            
    if HeavyScrape == False:  
        for member in UserList:
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
    else:
        while not client.is_closed:
            member = random.choice(UserList)
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
    
if ':' in token: 
    enp = token.split(':')
    p = subprocess.Popen(['python','bots/misc/joinServer.py',enp[0],enp[1],inviteLink],shell=True)
    p.wait()

    client.run(enp[0],enp[1], bot=False) 
else: 
    client.run(token, bot=False)