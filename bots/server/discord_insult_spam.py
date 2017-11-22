import urllib.request
import discord
import asyncio
import sys
from bs4 import BeautifulSoup
sys.path.append("./.")
from config import *

client = discord.Client()
token = sys.argv[1]

@client.event
async def on_ready():
    while not client.is_closed:
        html = urllib.request.urlopen("https://insult.mattbas.org/api/insult.html").read()
        soup = BeautifulSoup(html,"html.parser")
        insult_text = soup.find('h1')
        print(insult_text.text)
        await client.send_message(discord.Object(id=DiscordChannel), insult_text.text)
        await asyncio.sleep(0.7) # Changes how fast the messages are posted. (Anything under 0.7 tends to break it
    
client.run(token,bot=False)
