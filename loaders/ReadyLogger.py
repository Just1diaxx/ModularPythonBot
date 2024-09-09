import discord
from discord.ext import commands

class ReadyLogger:
    bot = commands.Bot
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    print("------------------------------")
    print(f"Logged as {bot.name}")
    print(f"Guilds: {int(bot.guilds)}")
    print(f"Invite link: https://discord.com/oauth2/authorize?client_id={bot.application_id}&permissions=8&integration_type=0&scope=bot")
    print("------------------------------")