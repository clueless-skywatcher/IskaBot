from iskabot.commands import *
from iskabot.utils import *

import discord

class HelpCommand(BaseCommand):
    name = "help"
    help_text = '''
    Produces a help text listing all bot commands. 
    If a command name is provided, it shows help for only that command
    '''

    @classmethod
    async def call(self, ctx, params):
        if len(params) > 1:
            await ctx.channel.send(f"Wrong command syntax")
            return
        await self.run(ctx, params)

    @classmethod
    async def run(self, ctx, params):
        commands = all_subclasses(BaseCommand)
        if len(params) > 0:
            cmd_name = params[0]
            cmd_found = False
            for cmd in commands:
                if cmd.name == cmd_name or cmd_name in cmd.aliases:
                    embed = discord.Embed(
                        title = "Help: " + ", ".join([cmd.name] + cmd.aliases),
                        description = cmd.help_text,
                        colour = discord.Colour.blue()
                    )
                    cmd_found = True
                    break
            if cmd_found == False:
                await ctx.channel.send("No help was found on this command.")
        else:
            embed = discord.Embed(
                title = "Commands documentation",
                description = '''
                    Here are all the help commands. 
                    Use iska. before each command
                ''',
                colour = discord.Colour.blue()
            )
            commands.remove(ActionGIFCommand)
            commands = sorted(commands, key = lambda x : x.name)
            for c in commands:
                embed.add_field(
                    name = ", ".join([c.name] + c.aliases),
                    value = c.help_text,
                    inline = False
                )
            embed.set_footer(text = "Made with love")
        await ctx.channel.send(embed = embed)

