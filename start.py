import sys
import subprocess
import os
from time import sleep
from config import *

w1 = "EDIT YOUR CONFIG.PY BEFORE USING!\n"

def worker(file,token):
    print(token + " " + file)
    subprocess.call(file, shell=True)

for char in w1:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
sleep(0.5)
print("Type one of the following numbers to launch that spammmer")
print("       +========-Server Spammers-=========+")
print("1 : Text Spammer - Write your own text to spam")
print("2 : Image Spammer - Spam random images in a selected folder")
print("3 : Insult Spammer - Picks insults offline and spams them")
print("         +========-DM Spammers-=========+      ")
print("4 : Text Spammer - Write your own text to spam")
print("5 : Image Spammer - Spam random images in a selected folder")
print("6 : Insult Spammer - Picks insults offline and spams them")

in_pick = float(input("Select a bot: "))

if in_pick == 1:
    spam_text = input("Write spam text : ")
    for token in userToken:
        p = subprocess.Popen(['python','bots\server\discord_text_spam.py',token,spam_text],shell=True)
        sleep(1)

if in_pick == 2:
    for token in userToken:
        p = subprocess.Popen(['python', 'bots\server\discord_image_spam.py', token],shell=True)
            
if in_pick == 3:
    for token in userToken:
        p = subprocess.Popen(['python','bots\server\discord_insult_spam.py', token],shell=True)
#DM Spammers
if in_pick == 4:
    if not os.path.exists('dm_spam_text.txt'):
        file = open('dm_spam_text.txt','w')
        file.write('=====Merubokkusu=====\n')#This is written for bug issues :/
        file.close()
    spam_text = input("Write spam text : ")
    for token in userToken:
        p = subprocess.Popen(['python','bots\DM\discord_text_spam_dm.py',token,spam_text],shell=True)
        sleep(2.5)

if in_pick == 5:
    if not os.path.exists('dm_spam_image.txt'):
        file = open('dm_spam_image.txt','w')
        file.write('=====Merubokkusu=====\n')#This is written for bug issues :/
        file.close()
    for token in userToken:
        p = subprocess.Popen(['python', 'bots\DM\discord_image_spam_dm.py', token],shell=True)
            
if in_pick == 6:
    if not os.path.exists('dm_spam_insult.txt'):
        file = open('dm_spam_insult.txt','w')
        file.write('=====Merubokkusu=====\n')#This is written for bug issues :/
        file.close()
    for token in userToken:
        p = subprocess.Popen(['python','bots\DM\discord_insult_spam_dm.py', token],shell=True)
p.wait()
