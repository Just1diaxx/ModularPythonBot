import discord
from base.BaseModule import BaseModule
from discord.ext import commands

class ExampleEvent(BaseModule):
    def __init__(self, bot: commands.Bot):
        super().__init__(bot)
    
    def setup(self):
        print("Module ExampleEvent loaded.")
    
    async def on_presence_update(self, before: discord.Member, after: discord.Member):
        print(f"Presence update: {after.name}")
    
    async def on_message(self, message: discord.Message):
        if(message.author != self.bot.user):
            print("Received a message!")
    
    async def on_guild_member_update(self, before: discord.Member, after: discord.Member):
        print(f"Guild member update: {after.name}")

    async def register_events(self):
        self.bot.add_listener(self.on_presence_update, 'on_presence_update')
        self.bot.add_listener(self.on_guild_member_update, 'on_guild_member_update')
        self.bot.add_listener(self.on_message, "on_message")

async def setup(bot: commands.Bot):
    module = ExampleEvent(bot)
    module.setup()
    await module.register_events()
