import discord

client = discord.Client()

@client.event 
async def on_ready():
    print("Bot is now online and ready to roll")

@client.event 
async def on_message(message):

    if (message.author == client.user):
        return 

    if (message.content == "hello"):
        await message.channel.send('Welcome bro')

client.run('ODk0NDgyNzkxNzc1OTkzODU2.YVqqBA.4m0BiWj5c3USfvpJDqM9cIXeDb4')