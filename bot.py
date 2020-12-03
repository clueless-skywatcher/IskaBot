import discord
from discord.ext import commands
from decouple import config

from iskabot.commands import *

DISCORD_BOT_TOKEN = config("DISCORD_BOT_TOKEN")

class IskaBot(commands.Bot):
    def __init__(self):
        commands.Bot.__init__(self,
                              command_prefix = '__',
                              self_bot = False,
                              intents = discord.Intents(
                messages = True,
                guilds = True,
                reactions = True,
                members = True,
                presences = True
            )
                              )
        self.message1 = "info: Bot online"
        self.message2 = "info: Bot online"

    async def on_ready(self):
        await self.change_presence(activity = discord.Game(name ="__help"))
        print(self.message1)

    async def on_message(self, message):
        ctx = await self.get_context(message = message)

        if message.content.startswith(self.command_prefix):
            cmd_whole = message.content[len(self.command_prefix):]
            cmd_actual = cmd_whole.split(" ")[0]
            cmd_params = cmd_whole.split(" ")[1:]
            cmd_found = False
            for cmd in BaseCommand.__subclasses__():
                if cmd.name == cmd_actual or cmd_actual in cmd.aliases:
                    cmd_found = True
                    await cmd.call(ctx, cmd_params)
                    break

            if cmd_found == False:
                await ctx.channel.send(f"Sorry, wrong command!")

if __name__ == '__main__':
    bot = IskaBot()
    bot.run(DISCORD_BOT_TOKEN)