from discord.ext import commands

class BaseModule:
    def __init__(self, bot):
        self.bot = bot

    async def setup(self):
        raise NotImplementedError("This method should be overridden.")

    async def register_events(self):
        raise NotImplementedError("This method should be overridden.")
