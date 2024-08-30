#    _____             .___    .__              __________          __  .__                 __________        __   
#   /     \   ____   __| _/_ __|  | _____ ______\______   \___.__._/  |_|  |__   ____   ____\______   \ _____/  |_ 
#  /  \ /  \ /  _ \ / __ |  |  \  | \__  \\_  __ \     ___<   |  |\   __\  |  \ /  _ \ /    \|    |  _//  _ \   __\
# /    Y    (  <_> ) /_/ |  |  /  |__/ __ \|  | \/    |    \___  | |  | |   Y  (  <_> )   |  \    |   (  <_> )  |  
# \____|__  /\____/\____ |____/|____(____  /__|  |____|    / ____| |__| |___|  /\____/|___|  /______  /\____/|__|  
#         \/            \/               \/                \/                \/            \/       \/             


import discord
from discord.ext import commands
from loaders.InitialLoader import InitialLoader

intents = discord.Intents.all()

class ModularPythonBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.initial_loader = InitialLoader(self)

    async def setup_hook(self):
        await self.initial_loader.load_all()
        
        synced = await self.tree.sync()
        print(f"Loader synced {len(synced)} commands.")

bot = ModularPythonBot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} is now in execution!')


bot.run("TOKEN HERE")
