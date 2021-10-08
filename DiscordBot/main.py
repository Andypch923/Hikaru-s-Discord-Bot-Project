import discord
import re
import random 
from random import randrange
from datetime import datetime


client = discord.Client()

@client.event 
async def on_ready():
    print("BOT IS NOW ONLINE")

@client.event 
async def on_message(message):

    if (message.author == client.user):
        return 

    if (re.search("!",message.content) != -1):
        endOfCmdFromUser = re.search("\s",message.content)
        cmdFromUser = message.content[1:endOfCmdFromUser];
        if (cmdFromUser == "8ball"):
            random.seed(datetime.now())
            randNum = randrange(10)+1
            switch(randNum)

def switch(argument):
    switcher = {
        1: "You are what you eat.",
        2: "There are plenty of sea in the fish.",
        3: "You don't want to know.",
        4: "Can I get some actual questions?",
        5: "Don't bother.",
        6: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        7: "You know what else you should ask about? My sponsor, RAID SHADOW LEGENDS.",
        8: "Pogchamp.",
        9: "Bananana~ Bananana~",
        10: ".-."
    }
    await message.channel.send(switcher)
client.run('')