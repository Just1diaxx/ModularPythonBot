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
