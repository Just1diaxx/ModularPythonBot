import discord
from discord import app_commands

class BaseCommand:
    def __init__(self, bot: discord.Client):
        self.bot = bot

    async def register(self):
        raise NotImplementedError("This method should be overridden.")
