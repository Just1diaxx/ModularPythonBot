#  _____ ______   ________  ________  ___  ___  ___       ________  ________          ________  ___    ___ _________  ___  ___  ________  ________           ________  ________  _________   
# |\   _ \  _   \|\   __  \|\   ___ \|\  \|\  \|\  \     |\   __  \|\   __  \        |\   __  \|\  \  /  /|\___   ___\\  \|\  \|\   __  \|\   ___  \        |\   __  \|\   __  \|\___   ___\ 
# \ \  \\\__\ \  \ \  \|\  \ \  \_|\ \ \  \\\  \ \  \    \ \  \|\  \ \  \|\  \       \ \  \|\  \ \  \/  / ||___ \  \_\ \  \\\  \ \  \|\  \ \  \\ \  \       \ \  \|\ /\ \  \|\  \|___ \  \_| 
#  \ \  \\|__| \  \ \  \\\  \ \  \ \\ \ \  \\\  \ \  \    \ \   __  \ \   _  _\       \ \   ____\ \    / /     \ \  \ \ \   __  \ \  \\\  \ \  \\ \  \       \ \   __  \ \  \\\  \   \ \  \  
#   \ \  \    \ \  \ \  \\\  \ \  \_\\ \ \  \\\  \ \  \____\ \  \ \  \ \  \\  \|       \ \  \___|\/  /  /       \ \  \ \ \  \ \  \ \  \\\  \ \  \\ \  \       \ \  \|\  \ \  \\\  \   \ \  \ 
#    \ \__\    \ \__\ \_______\ \_______\ \_______\ \_______\ \__\ \__\ \__\\ _\        \ \__\ __/  / /          \ \__\ \ \__\ \__\ \_______\ \__\\ \__\       \ \_______\ \_______\   \ \__\
#     \|__|     \|__|\|_______|\|_______|\|_______|\|_______|\|__|\|__|\|__|\|__|        \|__||\___/ /            \|__|  \|__|\|__|\|_______|\|__| \|__|        \|_______|\|_______|    \|__|
#                                                                                             \|___|/                                                                     


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
