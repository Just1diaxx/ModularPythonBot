import discord
from discord.ext import commands

class ReadyLogger():
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
        print("------------------------------")
        print(f"Logged as {bot.user}")
        print(f"Guilds: {len(bot.guilds)}")
        print(f"Invite link: https://discord.com/oauth2/authorize?client_id={bot.application_id}&permissions=8&integration_type=0&scope=bot")
        print("------------------------------")
