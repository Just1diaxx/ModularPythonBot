# ModularPythonBot

> Hi, this is a template of a discord.py bot for beginners.
> It is divided in various folders: ```modules``` and ```commands```.
> Modules are simply some event listeners and can be registered by ```self.bot.add_listener(function, "event")```. So, for example ```self.bot.add_listener(self.on_message, "on_message")```

Command template:

```python
import discord
from discord import app_commands
from base.BaseCommand import BaseCommand

class ExampleCommand(BaseCommand):
    def __init__(self, bot):
        super().__init__(bot)

    async def register(self):
        print("Command ExampleCommand loaded.")

        @app_commands.command(name="hello", description='Answers with "hello, user!".')
        async def hello(interaction: discord.Interaction):
            await interaction.response.send_message(f"Hello, {interaction.user.mention}!")

        self.bot.tree.add_command(hello)

def setup(bot):
    command = ExampleCommand(bot)
    return command.register()
```

Module template:

```python
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
```

Installation:

- 1: Download python 3.12+
- 2: Install discord.py, ```pip install discord```
- 3: Create a bot from the [Discord Developer Page](https://discord.com/developers/applications)
- 4: Paste the bot token into the code of bot.py
    ```python
    bot.run("TOKEN HERE") -> bot.run("nfdjsdhfiurhd.82njeh.uihwgsf78dsytfbe")
    ```
- 5: Ready to go! Just run ```python bot.py``` to execute the bot.

---

Fell free to fork this repo and make some updates, or if you don't know how programming, open an issue of suggestion!

