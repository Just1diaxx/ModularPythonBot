import os
from importlib import import_module

class ModulesLoader:
    def __init__(self, bot):
        self.bot = bot

    async def load_modules(self, modules_folder):
        if not os.path.exists(modules_folder):
            print(f"Error: The folder {modules_folder} doesn't exist.")
            return
        
        for filename in os.listdir(modules_folder):
            if filename.endswith('.py'):
                module_name = f'modules.{filename[:-3]}'
                try:
                    module = import_module(module_name)
                    await module.setup(self.bot)
                except Exception as e:
                    print(f"Error while loading the module {module_name}: {e}")
