import os
from importlib import import_module

class CommandsLoader:
    def __init__(self, bot):
        self.bot = bot

    async def load_commands(self, commands_folder):
        if not os.path.exists(commands_folder):
            print(f"Error: The folder {commands_folder} doesn't exist.")
            return
        for filename in os.listdir(commands_folder):
            if filename.endswith('.py'):
                try:
                    module_name = f'commands.{filename[:-3]}'
                    module = import_module(module_name)
                    await module.setup(self.bot)
                except Exception as e:
                    print(f"Error while loading the command {module_name}: {e}")
