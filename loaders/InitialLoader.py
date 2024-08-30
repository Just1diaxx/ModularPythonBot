from loaders.CommandsLoader import CommandsLoader
from loaders.ModulesLoader import ModulesLoader

class InitialLoader:
    def __init__(self, bot):
        self.bot = bot
        self.commands_loader = CommandsLoader(bot)
        self.modules_loader = ModulesLoader(bot)

    async def load_all(self):
        await self.modules_loader.load_modules("modules")
        await self.commands_loader.load_commands("commands")
        
        
