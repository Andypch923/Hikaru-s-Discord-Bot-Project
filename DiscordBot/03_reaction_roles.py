import discord

class MyClient(discord.Client):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 894526548315631637

    async def on_ready(self):
        print('Ready')

    async def on_raw_reaction_add(self,payload):
        '''Give a role based on reaction emoji'''
        if payload.message_id != self.target_message_id:
            return
        
        guild = client.get_guild(payload.guild_id)

        print(payload.emoji.name)

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents = intents)
client.run('ODk0NDgyNzkxNzc1OTkzODU2.YVqqBA.4m0BiWj5c3USfvpJDqM9cIXeDb4')